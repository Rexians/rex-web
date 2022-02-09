import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class PlayerDataBase():
    '''
    Used to access the Player DataBase.
    '''
    def __init__(self, discord_id):
        self.id = discord_id
        cluster_code = os.environ.get('cluster')
        cluster = MongoClient(cluster_code)
        self.db = cluster["MCOC"]["Account"]
        self.user_acc = self.db.find_one({'discord_id':discord_id}, {'_id':0})
        
    def check_acc_exist(self):
        '''
        Checks if a account exists/details are correct.
        ''' 
        if self.user_acc is None:
            return(False) #Account either doesn't exists or account details are wrong.
        else:
            return(True) #Account exists and/or details are correct.

    def create_account(self, game_name):
        if self.user_acc is None:
            acc_dict = {"game_name":game_name,
                        "discord_id":self.id,
                        "roster":[],   
                        }
            self.db.insert_one(acc_dict)
            return(True) #Account was created.
        else:
            return(False) #Account wasn't made as it already exists.
