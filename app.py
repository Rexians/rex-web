from flask import *
import qrcode
from pytube import YouTube
from src.speedtester import speed
from src.downloader import ytdownload

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",template_folder="templates")

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
    return render_template("qrcreate.html",template_folder="templates")

@app.route("/downloader/",methods = ['GET', 'POST'])
def downloader():
    if request.method == 'POST':
        yt = ytdownload()
        link = YouTube(request.form.get("ytlink"))
        filepath = yt.download(link)
        return render_template("video_watch.html",template_folder="templates", filetitle=link.title, filepath= filepath, thumbnail= link.thumbnail_url)
    return render_template("downloader.html", template_folder="templates")    

@app.route("/download/",methods = ['GET', 'POST'])
def download():
    if request.method == 'POST':
        filepath = request.form.get('filepath')
        return send_file(filepath, as_attachment=True)
    return redirect(url_for('downloader'))

@app.route("/speedtest/")
def speedtesting():
    st = speed()
    return (f"Download Speed-{st.downloads()}Bit/s\nUpload Speed-{st.uploads()}Bit/s\nPings-{st.pings()}\nHost Info-{st.host_infos()}\nIP-{st.ips()}")

if __name__ =='__main__':
    app.run(debug=True)  
