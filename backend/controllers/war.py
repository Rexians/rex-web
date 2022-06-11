from flask import Blueprint, jsonify, session
import requests
from models.war import War

war = Blueprint("war", __name__)

@war.route("/war/<tier>")
def get_war_info(tier: int):
    """
    Get war info based on tier provieded

    Args:
        tier (int): Tier of war

    Returns:
        response (Response): Return response of war info
    """
    war = War()
    war.get_war_info(tier)
    response = jsonify(war.war_info)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response