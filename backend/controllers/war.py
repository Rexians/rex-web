from flask import Blueprint, jsonify
import requests
from models.war import War

war = Blueprint("war", __name__)

@war.route("/war/<tier>")
def get_war_info(tier):
    war = War()
    war.get_war_info(tier)
    response = jsonify(war.war_info)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response