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
        self.users_collection.update_one({'user_id': self.user_id}, {'$set': {'roster': roster}})


    def add_champ(self, champ: dict):
        """
        Adds the champ to the roster

        Args:
            champ (dict): Dictionary of the champion
        """
        self.users_collection.update_one({'user_id': self.user_id}, {'$push': {'roster.champs': champ}})

        
    def get_champs_imgs(self):
        """
        Gets all users champs images to display in roster

        Returns:
            None: If user has no champs
            champ_imgs (list): List of all champ images
        """
        user_roster = self.users_collection.find_one({"user_id": self.user_id}, {"roster": 1, "_id": 0})
        if len(user_roster['roster']['champs']) == 0:
            return None
        champ_imgs = [champ['champ_img'] for champ in user_roster['roster']['champs']]
        return champ_imgs
    
    def get_latest_champ_img(self):
        user_roster = self.users_collection.find_one({"user_id": self.user_id}, {"roster": 1, "_id": 0})
        champ_img = user_roster['roster']['champs'][-1]['champ_img']
        return champ_img