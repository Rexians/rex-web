from flask import Blueprint, jsonify, request, session
from flask_cors import cross_origin
import requests
from models.champ import Champ
from models.user import User
from models.roster import Roster
from helpers.convert_name import convert

roster = Blueprint("roster", __name__)

@roster.route("/roster/add", methods=["POST"])
def add_champ():
    """
    Adds champ to roster

    Returns:
        response (Response): 201 - successful creation of resource at location
    """
    # Get champ params that user inputted
    params = request.args.to_dict()

    # All data being added
    champ_id = convert(params['champ'])
    tier = int(params['tier'])
    rank = int(params['rank'])
    try:
        stats = requests.get(f"http://127.0.0.1:8000/champs/?champ={champ_id}&tier={tier}&rank={rank}").json()
        champ_name = stats['name']
        champ_class = stats['class']
        prestige = stats['prestige']
        champ_img = stats['img_portrait']
    except:
        print("API DOWN")
        return ""

    champ = Champ(champ_id, champ_name, champ_class, tier, rank, prestige, champ_img).create_champ()
    
    # Add to roster
    Roster(session['user_id']).add_champ(champ)

    response = jsonify()
    response.status_code = 201
    response.headers['location'] = f"/roster/add/{session['token']}" 
    return response

@roster.route("/roster/champ")
@cross_origin(supports_credentials=True)
def get_champ():
    """
    Gets champ using the champ_id and tier that user selected

    Returns:
         response (Response): Dict of champ stats, success - 200
    """
    # Get champ params that user inputted
    params = request.args.to_dict()
    champ_id = params["champ-id"]
    tier = int(params["tier"])

    champ_info = Roster(session['user_id']).get_champ(champ_id, tier)

    response = jsonify({"champ_info": champ_info})
    response.status_code = 200
    return response

@roster.route("/roster/champs/imgs")
@cross_origin(supports_credentials=True)
def get_all_champs_display():
    """
    Get display info of all champs of user

    Returns:
        response (Response): List of champ displays info, success - 200
    """
    champ_display = Roster(session['user_id']).get_champs_display()
    response = jsonify({'display_info':champ_display})
    response.status_code = 200
    return response

@roster.route("/roster/champs/imgs/latest")
@cross_origin(supports_credentials=True)
def get_latest_champ_display():
    """
    Get latest added champ display info

    Returns:
        response (Response): Object of latest champ display info, success - 200 
    """
    champ_display = Roster(session['user_id']).get_latest_champ_display()
    response = jsonify({'display_info':champ_display})
    response.status_code = 200
    return response
