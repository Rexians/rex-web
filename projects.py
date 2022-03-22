import os

import qrcode
from dotenv import load_dotenv
from flask import (Flask, redirect, render_template, request, send_file,
                   session, url_for)
from pytube import YouTube

from helpers.downloader import ytdownload

load_dotenv()

token = os.environ.get('TOKEN')
client_secret = os.environ.get('CLIENT_SECRET')
redirect_uri = os.environ.get('REDIRECT_URI')
oauth_uri = os.environ.get('OAUTH_URI')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'IndominusRexian'

@app.route("/")
def home():
    return render_template("projects.html")

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
        url = yt.download(link)
        return render_template("video_watch.html", filetitle=link.title, filepath= url, thumbnail= link.thumbnail_url)
    return render_template("downloader.html", )    

@app.route("/download/",methods = ['GET', 'POST'])
def download():
    if request.method == 'POST':
        url = request.form.get('filepath')
        return send_file(url, as_attachment=True)
    return redirect(url_for('downloader'))

@app.route("/redirect/discord")
def redirect_discord():
    return render_template("discord_redirect.html", )

if __name__ =='__main__':
    app.run(debug=False)  