from models.user import User
from models.roster import Roster

def create_user(user_id):
    User(user_id).create_user()
    Roster(user_id).create_roster()
