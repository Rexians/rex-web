from flask import Flask, render_template, redirect, request, send_file, session, url_for
from pytube import YouTube
from dotenv import load_dotenv
from zenora import APIClient
from src.downloader import ytdownload
from src.database import PlayerDataBase
import qrcode
import os

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
    if 'token' in session:
        bearer_client = APIClient(session['token'], bearer=True)
        user = bearer_client.users.get_current_user()         
        return render_template("home.html", details=user)
    return render_template("home.html",)

@app.route("/test/")
def test():
    return "Test Page"

@app.route("/qrcreate/", methods =["GET", "POST"])
def qrcreate():
    if request.method == "POST":
        text_qr = request.form.get("textqr")
        qr = qrcode.make(f"{text_qr}")
        qr.save("qr_code.png")
        filename = "qr_code.png"
        return send_file(filename, mimetype='image/gif')
    return render_template("qrcreate.html",)

@app.route("/downloader/",methods = ['GET', 'POST'])
def downloader():
    if request.method == 'POST':
        yt = ytdownload()
        link = YouTube(request.form.get("ytlink"))
        filepath = yt.download(link)
        return render_template("video_watch.html", filetitle=link.title, filepath= filepath, thumbnail= link.thumbnail_url)
    return render_template("downloader.html", )    

@app.route("/download/",methods = ['GET', 'POST'])
def download():
    if request.method == 'POST':
        filepath = request.form.get('filepath')
        return send_file(filepath, as_attachment=True)
    return redirect(url_for('downloader'))

@app.route("/redirect/discord")
def redirect_discord():
    return render_template("discord_redirect.html", )

@app.route("/soon")
def soon():
    return render_template("soon.html", )

@app.route("/404")
def invalid_route_404():
    return render_template("404.html", )

@app.errorhandler(404) 
def invalid_route(e): 
    return render_template("404.html",templates_folder="templates")

@app.route('/login')
def login():
    if 'token' in session:
        bearer_client = APIClient(session['token'], bearer=True)
        user = bearer_client.users.get_current_user()
        return redirect('/profile')  
    return render_template('login.html', oauth_uri=oauth_uri)

@app.route('/oauth/callback')
def callback():
    try:
        code = request.args['code']
        access_token = client.oauth.get_access_token(code, redirect_uri).access_token
        session['token'] = access_token
        return redirect('/oauth/callback/gamename')
    except:
        return redirect('/login')

@app.route('/oauth/callback/gamename', methods=['GET', 'POST'])
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
                acc = db.create_account(gname)
                if acc == True: #Account has been created 
                    return redirect('/profile/redirect')
                else: #Account is already there.
                    return redirect('/login/redirect')  
        else:
            if user.id == details['discord_id']:
                return redirect('/profile')                          
        return render_template('gamename.html', user=user)
    return redirect('/login')    

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/profile')
def profile():
    if 'token' in session:
        bearer_client = APIClient(session['token'], bearer=True)
        user = bearer_client.users.get_current_user()          
        db = PlayerDataBase(user.id)
        details = db.get_account()
        return render_template('profile.html', show_details=True, title=details['game_name'], details=details, user=user)
    else:
        return redirect('/login')    

@app.route('/profile/redirect')
def profile_redirect():
    if 'token' in session:
        bearer_client = APIClient(session['token'], bearer=True)
        user = bearer_client.users.get_current_user()          
        db = PlayerDataBase(user.id)
        details = db.get_account()        
        return render_template('profile.html', redirect_success=True, show_details=True, title=details['game_name'], details=details, user=user)
    else:
        return redirect('/login')

@app.route('/addchamp', methods=['GET', 'POST'])
def champ_adder():
    if 'token' in session:
        bearer_client = APIClient(session['token'], bearer=True)
        user = bearer_client.users.get_current_user()          
        db = PlayerDataBase(user.id)
        details = db.get_account()  
        champ_names = db.get_fancy_champ_names()
        if 'POST' in request.method:
            champname = db.fancy_to_standard(request.form.get('champ-name'))
            print(champname)
            if champname != False:
                tier = int(request.form.get('champ-tier'))
                rank = int(request.form.get('champ-rank'))
                signature = int(request.form.get('champ-sig'))
                db.add_champ(champname, tier, rank, signature)
                if db.error != None:
                    return render_template('addchamp.html', error_status=True, error=db.error, title = user.username, details=details, champ_names=champ_names)
                elif db.details != None:
                    return render_template('addchamp.html', error_status=False, detail=db.details, title = user.username, details=details, champ_names=champ_names)    
        return render_template('addchamp.html', details=details, champ_names=champ_names, sigs=range(0,201), title = user.username)
    else:
        return redirect('/login')


if __name__ =='__main__':
    app.run(debug=False)  