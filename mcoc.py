import os

from dotenv import load_dotenv
from flask import (Flask, redirect, render_template, request,
                   session)
from zenora import APIClient

from helpers.database import AllianceDataBase, PlayerDataBase
from helpers.downloader import YT

load_dotenv()

token = os.environ.get('TOKEN')
client_secret = os.environ.get('CLIENT_SECRET')
redirect_uri = os.environ.get('REDIRECT_URI')
oauth_uri = os.environ.get('OAUTH_URI')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'IndominusRexian'
client = APIClient(token=token, client_secret=client_secret)

@app.route("/")
def home():
    yt = YT()
    links = yt.get_mcoc_links()
    if 'token' in session:
        bearer_client = APIClient(session['token'], bearer=True)
        user = bearer_client.users.get_current_user()         
        return render_template("mcoc.html", details=user, youtube_links=links)
    return render_template("mcoc.html", youtube_links=links)

@app.route("/redirect/discord/")
def redirect_discord():
    return render_template("discord_redirect.html", )

@app.route("/soon/")
def soon():
    return render_template("soon.html", )

@app.route("/404/")
def invalid_route_404():
    return render_template("404.html", )

@app.errorhandler(404) 
def invalid_route(e): 
    return render_template("404.html",templates_folder="templates")

@app.route('/login/')
def login():
    if 'token' in session:
        bearer_client = APIClient(session['token'], bearer=True)
        user = bearer_client.users.get_current_user()
        return redirect('/profile/')  
    return render_template('login.html', oauth_uri=oauth_uri)

@app.route('/oauth/callback/')
def callback():
    try:
        code = request.args['code']
        access_token = client.oauth.get_access_token(code, redirect_uri).access_token
        session['token'] = access_token
        return redirect('/oauth/callback/gamename/')
    except:
        return redirect('/login/')

@app.route('/oauth/callback/gamename/', methods=['GET', 'POST'])
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
                    print(dbs)
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
                return redirect('/profile/')                          
        return render_template('gamename.html', user=user)
    return redirect('/login/')    

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/login/')

@app.route('/profile/')
def profile():
    if 'token' in session:
        bearer_client = APIClient(session['token'], bearer=True)
        user = bearer_client.users.get_current_user()          
        db = PlayerDataBase(user.id)
        details = db.get_account()
        return render_template('profile.html', show_details=True, title=details['game_name'], details=details, user=user)
    else:
        return redirect('/login/')    

@app.route('/profile/redirect/')
def profile_redirect():
    if 'token' in session:
        bearer_client = APIClient(session['token'], bearer=True)
        user = bearer_client.users.get_current_user()          
        db = PlayerDataBase(user.id)
        details = db.get_account()        
        return render_template('profile.html', redirect_success=True, show_details=True, title=details['game_name'], details=details, user=user)
    else:
        return redirect('/login/')

@app.route('/addchamp/', methods=['GET', 'POST'])
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

@app.route('/users/')
def users():
    db = PlayerDataBase()
    users_data = db.get_users_data()   
    return render_template('users.html', users_data=users_data)

@app.route('/user/') #/user?id=blabla
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

@app.route('/alliance/create/', methods=['GET', 'POST'])
def alliance():
    if 'token' in session:
        if 'POST' in request.method:
            ally_name = request.form.get('ally-name')
            ally_tag = request.form.get('ally-tag')
            print(ally_name, ally_tag)
        return render_template('alliance_create.html')
    else:
        return redirect('/login/')    
        
if __name__ =='__main__':
    app.run(debug=True)  
