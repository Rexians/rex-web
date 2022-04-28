from flask import Flask
from controllers.war import war

app = Flask(__name__)
app.register_blueprint(war)