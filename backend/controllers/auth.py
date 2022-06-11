import os
from dotenv import load_dotenv
import requests
from flask import Blueprint, jsonify, session, redirect, request
from flask_cors import cross_origin
from helpers.create_user import create_user

load_dotenv()

auth = Blueprint('Auth', __name__)

API_ENDPOINT = 'https://discord.com/api/v9'
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = os.environ.get('REDIRECT_URI')

@auth.route('/oauth/callback')
@cross_origin(supports_credentials=True)
def exchange_code():
    """
    OAuth2 implementation using Discord

    Returns:
        _type_: redirect to /auth 
    """
    code = request.args['code']
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Get access token information after user logs in
    r = requests.post(f"{API_ENDPOINT}/oauth2/token", data=data, headers=headers)
    r.raise_for_status()
    r = r.json()

    # Set access token in session and make it permanent  
    access_token = r['access_token']
    session['token'] = access_token
    session.permanent = True
    
    # Get user info from Discord API with access token
    headers = {"Authorization": "Bearer " + access_token}
    user_info = requests.get(f"{API_ENDPOINT}/users/@me", headers=headers).json()

    # Store discord id as user_id in session
    discord_id = user_info['id']
    session["user_id"] = discord_id 

    # Create the user
    create_user(session["user_id"])

    return redirect('http://localhost:3000/auth')


@auth.route('/authenticated')
@cross_origin(supports_credentials=True)
def is_authenticated():
    """
    Checks if user is logged in

    Returns:
        response (Response): response used in local storage
    """
    if 'token' in session:
        response = jsonify({"logged":True})
    else:
        response = jsonify({"logged":False})
    return response


@auth.route('/logout', methods=['POST'])
@cross_origin(supports_credentials=True)
def logout():
    """
    Log user out by clearing session

    Returns:
        response (Response): 204 - successfully fulfilled request  
    """
    if request.method == 'POST':
        session.clear()
        return ('', 204)
