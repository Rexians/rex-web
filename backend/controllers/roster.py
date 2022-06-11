from flask import Blueprint, jsonify, request, session
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
    stats = requests.get(f"http://127.0.0.1:8000/champs/?champ={champ_id}&tier={tier}&rank={rank}").json()
    champ_name = stats['name']
    champ_class = stats['class']
    prestige = stats['prestige']

    champ = Champ(champ_id, champ_name, champ_class, tier, rank, prestige).create_champ()
    
    # Add to roster
    Roster(session["user_id"]).add_champ(champ)

    response = jsonify()
    response.status_code = 201
    response.headers['location'] = f"/roster/add/{session['token']}" 
    return response