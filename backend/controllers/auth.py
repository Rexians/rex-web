import os
from dotenv import load_dotenv
import requests
from flask import Blueprint, jsonify, session, redirect, request

load_dotenv()

login = Blueprint('Login', __name__)

API_ENDPOINT = 'https://discord.com/api/v9'     
TOKEN = os.environ.get('TOKEN')
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = os.environ.get('REDIRECT_URI')

@login.route('/oauth/callback/')
def exchange_code():
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
    r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
    r.raise_for_status()
    r = r.json()

    access_token = r['access_token']
    session['token'] = access_token
    print(access_token)
    print(session)
    return redirect('http://localhost:3000/auth')


@login.route('/authenticated')
def is_authenticated():
    print(session)
    if 'token' in session:
        response = jsonify({"logged":True})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        response = jsonify({"logged":False})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response