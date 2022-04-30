import os
from dotenv import load_dotenv
from flask import (Blueprint, redirect, render_template, request,
                   session, url_for)
from zenora import APIClient

from helpers.database import PlayerDataBase

load_dotenv()

roster = Blueprint('Routes related to Rosters and users!', __name__)

token = os.environ.get('TOKEN')
client_secret = os.environ.get('CLIENT_SECRET')
redirect_uri = os.environ.get('REDIRECT_URI')
oauth_uri = os.environ.get('OAUTH_URI')

client = APIClient(token=token, client_secret=client_secret)

@roster.route('/login/')
def login():
    if 'token' in session:
        return redirect('/profile/')  
    return render_template('login.html', oauth_uri=oauth_uri)

@roster.route('/oauth/callback/')
def callback():
    try:
        code = request.args['code']
        access_token = client.oauth.get_access_token(code, redirect_uri).access_token
        session['token'] = access_token
        return redirect('/oauth/callback/gamename/')
    except Exception as e:
        print(e)
        return redirect('/login/')

@roster.route('/oauth/callback/gamename/', methods=['GET', 'POST'])
def gamename(): 
    if 'token' in session:
        bearer_client = APIClient(session['token'], bearer=True)
        user = bearer_client.users.get_current_user()  
        db = PlayerDataBase(user.id)
        details = db.get_account()
        if details == False:
            if request.method == 'POST':
                gname = request.form.get('gname')
                db = PlayerDataBase(user.id)
                dbs = db.get_users_data()
                redir = False
                for dicts in dbs:
                    if dicts['game_name'] == gname:
                        print('Exists')
                        redir = True
                        return render_template('gamename.html', error='Gamename exists!', user=user)
                if redir == False:
                    acc = db.create_account(gname, user)
                    if acc == True: #Account has been created                         
                        return redirect('/profile/redirect/')
                    else: #Account is already there.
                        return redirect('/login/redirect/')
        else:
            if user.id == details['discord_id']:
                ally_token = details['alliance']
                if ally_token is not None:
                    session['ally_token'] = ally_token
                    db.add_ally_token(ally_token)                
                return redirect('/profile/')                          
        return render_template('gamename.html', user=user)
    return redirect('/login/')    

@roster.route('/logout/')
def logout():
    session.clear()
    return redirect('/login/')

@roster.route('/profile/')
def profile():
    if 'token' in session:
        bearer_client = APIClient(session['token'], bearer=True)
        user = bearer_client.users.get_current_user()          
        db = PlayerDataBase(user.id)
        details = db.get_account()
        return render_template('profile.html', show_details=True, title=details['game_name'], details=details, user=user)
    else:
        return redirect('/login/')    

@roster.route('/profile/redirect/')
def profile_redirect():
    if 'token' in session:
        bearer_client = APIClient(session['token'], bearer=True)
        user = bearer_client.users.get_current_user()          
        db = PlayerDataBase(user.id)
        details = db.get_account()        
        return render_template('profile.html', redirect_success=True, show_details=True, title=details['game_name'], details=details, user=user)
    else:
        return redirect('/login/')

@roster.route('/addchamp/', methods=['GET', 'POST'])
def champ_adder():
    if 'token' in session:
        bearer_client = APIClient(session['token'], bearer=True)
        user = bearer_client.users.get_current_user()          
        db = PlayerDataBase(user.id)
        details = db.get_account()  
        champ_names = db.get_fancy_champ_names()
        if 'POST' in request.method:
            champname = db.fancy_to_standard(request.form.get('champ-name'))
            tier = request.form.get('champ-tier')
            rank = request.form.get('champ-rank')
            signature = request.form.get('champ-sig')  
            checker = [champname, tier, rank, signature]  
            if None not in checker:
                tier = int(tier)
                rank = int(rank)
                signature =int(signature)
                
                db.add_champ(champname, tier, rank, signature, user)
                if db.error != None:
                    return render_template('addchamp.html', error_status=True, error=db.error, title = user.username, details=details, champ_names=champ_names, sigs=range(0,201))
                elif db.details != None:
                    return render_template('addchamp.html', error_status=False, detail=db.details, title = user.username, details=details, champ_names=champ_names, sigs=range(0,201))    
            else:
                return render_template('addchamp.html', error_status=True, error='One or more fields was empty!', title = user.username, details=details, champ_names=champ_names, sigs=range(0,201))    
        return render_template('addchamp.html', details=details, champ_names=champ_names, sigs=range(0,201), title = user.username)
    else:
        return redirect('/login/')

@roster.route('/users/')
def users():
    db = PlayerDataBase()
    users_data = db.get_users_data()   
    return render_template('users.html', users_data=users_data)

@roster.route('/user/') #/user?id=blabla
def user():
    try:
        user_id = request.args.get('id')
        if user_id is not None:
            if 'token' in session:
                db = PlayerDataBase()
                ids_list = db.get_ids()
                if int(user_id) in ids_list:
                    db = PlayerDataBase(int(user_id))
                    details = db.get_account()
                    return render_template('user.html', details=details)
                else:
                    return 'Player Not Found!'    
            else:
                return redirect('/login/')    
        else:        
            raise LookupError
    except LookupError:
        return render_template('404.html')
