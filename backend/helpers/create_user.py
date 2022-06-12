from models.user import User
from models.roster import Roster

def create_user(user_id):
    """
    Create user function. If new user, also create roster

    Args:
        user_id (str): User id
    """
    if User(user_id).create_user():
        Roster(user_id).create_roster()
