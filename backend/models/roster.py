from models.user import User

class Roster(User):
    
    def __init__(self, discord_id):
        super().__init__(discord_id)
        self.champs: list = []
        self.total_prestige: int = 0
        self.total_champs: int = 0

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
        Adds the champ to the roster, 
        incrememnt total champs by 1, 
        and increment total prestige by champ prestige

        Args:
            champ (dict): Dictionary of the champion
        """
        self.users_collection.update_one({'user_id': self.user_id}, {'$push': {'roster.champs': champ}})
        self.users_collection.update_one({'user_id': self.user_id}, {'$inc': {'roster.total_champs': 1}})
        self.users_collection.update_one({'user_id': self.user_id}, {'$inc': {'roster.total_prestige': champ["prestige"]}})

    def get_champ(self, champ_id, tier):
        """
        Searches through user's champs and finds match of champ with champ_id AND tier
        Gets stats of that champ

        Args:
            champ_id (str): id of champ
            tier (int): tier of champ

        Returns:
            champ_info (dict): Dictionary of champ information if found
        """
        champ_info = None

        champ = self.users_collection.aggregate(
            [
            {'$limit': 1},
            {'$match': {'user_id': self.user_id}},
            {'$project': {
                '_id': 0,
                'roster.champs': {
                    '$filter': {
                        'input':'$roster.champs',
                        'as': 'champ',
                        'cond': {'$and':[
                                        {'$eq': [ '$$champ.tier', tier ]},
                                        {'$eq': [ '$$champ.champ_id', champ_id ]}
                                    ]
                                }
                        }
                    }
                }
            }
            ]
            )  

        for c in champ:
            champ_info = c['roster']['champs'][0]

        return champ_info
       
    def get_champs_display(self):
        """
        Gets all users champs display info in roster

        Returns:
            None: If user has no champs
            all_champ_displays (list): List of objects of each champs (img, tier, class)
        """
        all_champ_displays = []
        user_roster = self.users_collection.find_one({"user_id": self.user_id}, {"roster": 1, "_id": 0})

        if len(user_roster['roster']['champs']) == 0:
            return None

        for champ in user_roster['roster']['champs']:
            champ_display = {}
            champ_display["champ_id"] = champ["champ_id"]
            champ_display["champ_img"] = champ["champ_img"]
            champ_display["tier"] = champ["tier"]
            champ_display["champ_class"] = champ["champ_class"]
            all_champ_displays.append(champ_display)
       
        return all_champ_displays
    
    def get_latest_champ_display(self):
        """
        Gets latest champ display info

        Returns:
            champ_imgs (str): String of link to image
        """
        user_roster = self.users_collection.find_one({"user_id": self.user_id}, {"roster": 1, "_id": 0})

        champ = user_roster['roster']['champs'][-1]

        champ_display = {}
        champ_display["champ_id"] = champ["champ_id"]
        champ_display["champ_img"] = champ["champ_img"]
        champ_display["tier"] = champ["tier"]
        champ_display["champ_class"] = champ["champ_class"]

        return champ_display