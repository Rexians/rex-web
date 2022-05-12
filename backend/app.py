import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from controllers.auth import login
from controllers.war import war

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.register_blueprint(login)
app.register_blueprint(war)