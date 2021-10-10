from flask import *
import qrcode
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",template_folder="templates")

@app.route("/test")
def test():
    return "Test Page"

@app.route("/qrcreate", methods =["GET", "POST"])
def qrcreate():
    if request.method == "POST":
        text_qr = request.form.get("textqr")
        qr = qrcode.make(f"{text_qr}")
        qr.save("qr_code.png")
        filename = "qr_code.png"
        return send_file(filename, mimetype='image/gif')
    return render_template("qrcreate.html",template_folder="templates")

if __name__ =='__main__':
    app.run(debug=True)  