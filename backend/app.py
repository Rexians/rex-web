import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from controllers.auth import auth
from controllers.war import war
from controllers.roster import roster

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.register_blueprint(auth)
app.register_blueprint(war)
app.register_blueprint(roster)