from models.user import User

class Roster(User):
    
    def __init__(self, discord_id):
        super().__init__(discord_id)
        self.champs = []
        self.total_prestige = 0
        self.total_champs = 0

    def create_roster(self):
        """
        Creates the roster
        """

        roster = {"champs": self.champs, 
                "total_prestige": self.total_prestige, 
                "total_champs": self.total_champs}
        self.users_collection.update_one({"user_id": self.user_id}, {'$set': {"roster": roster}})


    def add_champ(self, champ: dict):
        """
        Adds the champ to the roster

        Args:
            champ (dict): Dictionary of the champion
        """
        self.users_collection.update_one({"user_id": self.user_id}, {'$push': {"roster.champs": champ}})