from flask import (Flask, render_template, session)
from zenora import APIClient

from helpers.downloader import YT
from routes.alliance import alliance
from routes.roster import roster

app = Flask(__name__, static_folder='./assets')
app.config['SECRET_KEY'] = 'IndominusRexian'
app.register_blueprint(alliance)
app.register_blueprint(roster)

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

if __name__ =='__main__':
    app.run(debug=False)  