import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from controllers.auth import auth
from controllers.war import war

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)
app.register_blueprint(auth)
app.register_blueprint(war)