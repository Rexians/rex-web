from database.database import Database

class User(Database):

    def __init__(self, discord_id):
        self.users_collection = Database.db['users']
        self.user_id = discord_id
        self.roster = {}

    def create_user(self):
        """
        Creates User

        Returns:
            Boolean : True if user is creates, false if user is already in database
        """
        # If user not in db, create, otherwise don't
        if not self.users_collection.find_one({"user_id": self.user_id}):
            user = {"user_id": self.user_id,
                    "roster": self.roster}
            self.users_collection.insert_one(user)
            return True
        else:
            print("User already in database")
            return False
