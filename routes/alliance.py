import random
import secrets

from datetime import datetime
from helpers.database import PlayerDataBase, AllianceDataBase
from flask import (Blueprint, redirect, render_template, request,
                   session, url_for)
from zenora import APIClient

alliance = Blueprint('Routes related to Alliances', __name__)

@alliance.route('/alliance/create/', methods=['GET', 'POST'])
def alliance_create():
    if 'token' in session:
        if 'ally_token' in session:
            return redirect('/alliance/')
        else:    
            if 'POST' in request.method:
                db = AllianceDataBase()
                bearer_client = APIClient(session['token'], bearer=True)
                user = bearer_client.users.get_current_user()                                              
                db2 = PlayerDataBase(user.id)
                leader_profile = db2.get_account()
                ally_name = request.form.get('ally-name')
                ally_tag = request.form.get('ally-tag')
                num = random.randint(16,1024)
                ally_token = secrets.token_urlsafe(num)
                now = datetime.now()
                date = now.strftime("%m/%d/%Y")
                create_ally = db.create_ally(ally_name, ally_tag, ally_token, date, leader_profile)
                if create_ally == True:
                    session['ally_token'] = ally_token
                    db2.add_ally_token(ally_token)
                    return redirect('/alliance/')
                else:
                    return redirect('/alliance/create')
        return render_template('alliance_create.html')
    else:
        return redirect('/login/')    

@alliance.route('/alliance/leave/')
def alliance_leave():
    if 'token' in session:
        if 'ally_token' in session:
            bearer_client = APIClient(session['token'], bearer=True)
            user = bearer_client.users.get_current_user()  
            db = PlayerDataBase(user.id)
            db2 = AllianceDataBase()
            leave = db.leave_ally()
            leave2 = db2.leave_ally()
            if leave == True:
                if leave2 == True:
                    session.pop('ally_token')
                    print('Removed')
                    return('Done!')
                else:
                    return redirect('/alliance/')    
            else:
                return redirect('/alliance/')    
        else:
            return redirect('/alliance/join/')            
    else:
        return redirect('/login/')

@alliance.route('/alliance/join/invite/', methods=['GET', 'POST']) #/?token=blabla
def alliance_join_invite():
    if 'token' in session:  
        if 'ally_token' in session:
            return redirect('/alliance/')
        else:
            ally_token = request.args.get('token')
            bearer_client = APIClient(session['token'], bearer=True)
            user = bearer_client.users.get_current_user()  
            db = AllianceDataBase()
            db2 = PlayerDataBase(user.id)
            data = db.get_details(ally_token)   
            user_data = db2.get_account()              
            if data is not False:
                session['ally_token'] = data['ally_token']
                db.add_member(ally_token, user_data)
                db2.add_ally_token(ally_token)
                return redirect('/alliance/') 
            else:
                return('Wrong Token!')                      
    else:        
        return redirect('/login/')

@alliance.route('/alliance/') 
def alliance_page():
    if 'token' in session:
        if 'ally_token' in session:
            db = AllianceDataBase()
            details = db.get_details(session['ally_token'])               
            return render_template('alliance.html', details=details)    
        else:
            return redirect('/alliance/join/')    
    else:
        return redirect('/login/')            

@alliance.route('/alliance/settings/')
def alliance_settings():
    if 'token' in session:
        if 'ally_token' in session:
            return(f'To Invite members, Share this <a href=/alliance/join/invite/?token={session["ally_token"]}>link</a>')
        else:
            return redirect('/alliance/join/')    
    else:
        return redirect('/login/')               

@alliance.route('/alliance/promote/', methods=['GET', 'POST'])
def alliance_promote():
    if 'token' in session:
        if 'ally_token' in session:
            db = AllianceDataBase()
            details = db.get_details(session['ally_token'])
            if details is not False:
                leader = details['members']['leader'] #dict
                officers = details['members']['officers'] #list of dicts
                members = details['members']['members'] #list of dicts
                return render_template('alliance_promote.html', details=details, leader=leader, officers=officers, members=members)
        else:
            return redirect('/alliance/join/')
    else:
        return redirect('/login/')            

