import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
from operator import itemgetter

class PlayerDataBase():
    '''
    Used to access the Player DataBase.
    '''
    def __init__(self, discord_id=None):
        self.id = discord_id
        cluster_code = os.environ.get('CLUSTER')
        cluster = MongoClient(cluster_code)
        self.cluster = cluster
        self.db = cluster["MCOC"]["Account"]
        self.user_acc = self.db.find_one({'discord_id':discord_id}, {'_id':0})
        self.error = None
        self.details = None
        
    def check_acc_exist(self):
        '''
        Checks if a account exists/details are correct.
        ''' 
        if self.user_acc is None:
            return(False) #Account either doesn't exists or account details are wrong.
        else:
            return(True) #Account exists and/or details are correct.

    def create_account(self, game_name, user):
        '''
        Creates an account in the DB. Returns False if the account wasn't made. 
        '''
        if self.user_acc is None:
            acc_dict = {"game_name":game_name,
                        "discord_id":self.id,
                        "avatar_url": user.avatar_url,
                        "prestige":0,
                        "about_me":None,
                        "alliance":None,
                        "roster":[],   
                        }
            self.db.insert_one(acc_dict)
            return(True) #Account was created.
        else:
            return(False) #Account wasn't made as it already exists.

    def get_account(self): 
        '''
        Gives account details. If account details weren't found, False is returned.
        '''        
        if self.user_acc is not None:
            return(self.user_acc)
        else:
            return(False)  

    def get_fancy_champ_names(self):
        champ_name_list = ['ABOMINATION', 'ABOMINATION (IMMORTAL)', 'ÆGON', 'AGENT VENOM', 'AIR-WALKER', 'AMERICA CHAVEZ', 'ANGELA', 'ANNIHILUS', 'ANT-MAN', 'ANTI-VENOM', 'APOCALYPSE', 'ARCHANGEL', 'BEAST', 'BISHOP', 'BLACK BOLT', 'BLACK PANTHER', 'BLACK PANTHER (CIVIL WAR)', 'BLACK WIDOW', 'BLACK WIDOW (CLAIRE VOYANT)', 'BLACK WIDOW (DEADLY ORIGIN)', 'BLADE', 'CABLE', 'CAPTAIN AMERICA', 'CAPTAIN AMERICA (INFINITY WAR)', 'CAPTAIN AMERICA (SAM WILSON)', 'CAPTAIN AMERICA (WWII)', 'CAPTAIN MARVEL', 'CAPTAIN MARVEL (CLASSIC)', 'CARNAGE', 'CIVIL WARRIOR', 'COLOSSUS', 'CORVUS GLAIVE', 'COSMIC GHOST RIDER', 'CROSSBONES', 'CULL OBSIDIAN', 'CYCLOPS (BLUE TEAM)', 'CYCLOPS (NEW XAVIER SCHOOL)', 'DAREDEVIL (CLASSIC)', "DAREDEVIL (HELL'S KITCHEN)", 'DARKHAWK', 'DEADPOOL', 'DEADPOOL (X-FORCE)', 'DIABLO', 'DOCTOR DOOM', 'DOCTOR OCTOPUS', 'DOCTOR STRANGE', 'DOCTOR VOODOO', 'DOMINO', 'DORMAMMU', 'DRAGON MAN', 'DRAX', 'EBONY MAW', 'ELECTRO', 'ELEKTRA', 'ELSA BLOODSTONE', 'EMMA FROST', 'FALCON', 'GAMBIT', 'GAMORA', 'GHOST', 'GHOST RIDER', 'GOLDPOOL', 'GREEN GOBLIN', 'GROOT', 'GUARDIAN', 'GUILLOTINE', 'GUILLOTINE 2099', 'GWENPOOL', 'HAVOK', 'HAWKEYE', 'HEIMDALL', 'HELA', 'HERCULES', 'HIT-MONKEY', 'HOWARD THE DUCK', 'HULK', 'HULK (IMMORTAL)', 'HULK (RAGNAROK)', 'HULKBUSTER', 'HUMAN TORCH', 'HYPERION', 'ICEMAN', 'IKARIS', 'INVISIBLE WOMAN', 'IRON FIST', 'IRON FIST (IMMORTAL)', 'IRON MAN', 'IRON MAN (INFINITY WAR)', 'IRON PATRIOT', 'JABARI PANTHER', 'JOE FIXIT', 'JUBILEE', 'JUGGERNAUT', 'KANG', 'KARNAK', 'KILLMONGER', 'KING GROOT', 'KINGPIN', 'KITTY PRYDE', 'KNULL', 'KORG', 'KRAVEN', 'LOKI', 'LONGSHOT', 'LUKE CAGE', 'MISTY KNIGHT', 'M.O.D.O.K.', 'MAGIK', 'MAGNETO', 'MAGNETO (HOUSE OF X)', 'MAN-THING', 'MANGOG', 'MASACRE', 'MEDUSA', 'MEPHISTO', 'MISTER FANTASTIC', 'MISTER NEGATIVE', 'MISTER SINISTER', 'MOJO', 'MOLE MAN', 'MOON KNIGHT', 'MORDO', 'MORNINGSTAR', 'MS. MARVEL', 'MS. MARVEL (KAMALA KHAN)', 'MYSTERIO', 'NAMOR', 'NEBULA', 'NICK FURY', 'NIGHT THRASHER', 'NIGHTCRAWLER', 'NIMROD', 'NOVA', 'ODIN', 'OLD MAN LOGAN', 'OMEGA RED', 'PENI PARKER', 'PHOENIX', 'PLATINUMPOOL', 'PROFESSOR X', 'PROXIMA MIDNIGHT', 'PSYCHO-MAN', 'PSYLOCKE', 'PUNISHER', 'PUNISHER 2099', 'PURGATORY', 'QUAKE', 'RED GOBLIN', 'RED GUARDIAN', 'RED HULK', 'RED SKULL', 'RHINO', 'ROCKET RACCOON', 'ROGUE', 'RONAN', 'RONIN', 'SABRETOOTH', 'SASQUATCH', 'SAURON', 'SCARLET WITCH', 'SCARLET WITCH (CLASSIC)', 'SENTINEL', 'SENTRY', 'SERSI', 'SHANG-CHI', 'SHE-HULK', 'SILVER CENTURION', 'SILVER SURFER', 'SORCERER SUPREME', 'SPIDER-GWEN', 'SPIDER-HAM', 'SPIDER-MAN (CLASSIC)', 'SPIDER-MAN (MILES MORALES)', 'SPIDER-MAN (STARK ENHANCED)', 'SPIDER-MAN (STEALTH SUIT)', 'SPIDER-MAN (SYMBIOTE)', 'SPIDER-MAN 2099', 'SQUIRREL GIRL', 'STAR-LORD', 'STORM', 'STORM (PYRAMID X)', 'STRYFE', 'SUNSPOT', 'SUPER-SKRULL', 'SUPERIOR IRON MAN', 'SYMBIOTE SUPREME', 'TASKMASTER', 'TERRAX', 'THANOS', 'THE CHAMPION', 'THE HOOD', 'THE OVERSEER', 'THING', 'THOR', 'THOR (JANE FOSTER)', 'THOR (RAGNAROK)', 'TIGRA', 'TOAD', 'ULTRON', 'ULTRON', 'UNSTOPPABLE COLOSSUS', 'VENOM', 'VENOM THE DUCK', 'VENOMPOOL', 'VISION', 'VISION (AARKUS)', 'VISION (AGE OF ULTRON)', 'VOID', 'VULTURE', 'WAR MACHINE', 'WARLOCK', 'WASP', 'WINTER SOLDIER', 'WOLVERINE', 'WOLVERINE (WEAPON X)', 'WOLVERINE (X-23)', 'YELLOWJACKET', 'YONDU']
        return champ_name_list

    def get_champ_names(self):
        champs_list = ['abomination', 'abomination_immortal', 'aegon', 'agentvenom', 'airwalker', 'americachavez', 'angela', 'annihilus', 'antman', 'antivenom', 'apocalypse', 'archangel', 'beast', 'bishop', 'blackbolt', 'blackpanther', 'blackpanther_cw', 'blackwidow', 'blackwidow_timely', 'blackwidow_movie', 'blade', 'cable', 'captainamerica', 'captainamerica_movie', 'captainamerica_samwilson' ,'captainamerica_ww2', 'captainmarvel_movie', 'captainmarvel', 'carnage', 'civilwarrior', 'colossus', 'corvusglaive', 'ghostrider_cosmic', 'crossbones', 'cullobsidian', 'cyclops_90s', 'cyclops', 'daredevil', 'daredevil_netflix', 'darkhawk', 'deadpool', 'deadpool_xforce', 'diablo', 'doctordoom', 'doc_ock', 'drstrange', 'brothervoodoo', 'domino', 'dormammu', 'dragonman', 'drax', 'ebonymaw', 'electro', 'elektra', 'elsabloodstone', 'emmafrost', 'falcon', 'gambit', 'gamora', 'ghost', 'ghostrider', 'deadpool_gold', 'green_goblin', 'groot', 'guardian', 'guillotine', 'guillotine_2099', 'gwenpool', 'havok', 'hawkeye', 'heimdall', 'hela', 'hercules', 'hitmonkey', 'howardmech', 'hulk', 'hulk_immortal', 'hulk_ragnarok', 'hulkbuster_movie', 'humantorch', 'hyperion', 'iceman', 'ikaris', 'invisiblewoman', 'ironfist', 'ironfist_white', 'ironman', 'ironman_movie', 'ironpatriot', 'blackpanther_realm', 'joefixit', 'jubilee', 'juggernaut', 'kang', 'karnak', 'killmonger', 'groot_king', 'kingpin', 'kittypryde', 'knull', 'korg', 'kraven', 'loki', 'longshot', 'lukecage', 'mistyknight' ,'modok', 'magik', 'magneto', 'magneto_marvelnow', 'manthing', 'mangog', 'masacre', 'medusa', 'mephisto', 'mrfantastic', 'misternegative', 'mistersinister', 'mojo', 'moleman', 'moonknight', 'karlmordo', 'morningstar', 'msmarvel', 'msmarvel_kamala', 'mysterio', 'namor', 'nebula', 'nickfury', 'nightthrasher', 'nightcrawler', 'nimrod', 'nova', 'odin', 'wolverine_oldman', 'omegared', 'peniparker', 'phoenix', 'deadpool_platinum', 'professorx', 'proximamidnight', 'psychoman', 'psylocke', 'punisher', 'punisher_2099', 'purgatory', 'quake', 'red_goblin', 'redguardian', 'hulk_red', 'redskull', 'rhino', 'rocket', 'rogue', 'ronan', 'ronin', 'sabretooth', 'sasquatch', 'sauron', 'scarletwitch_current', 'scarletwitch', 'sentinel', 'sentry', 'sersi', 'shangchi', 'shehulk', 'ironman_silvercenturion', 'silversurfer', 'drstrange_realm', 'spidergwen', 'spiderham', 'spiderman', 'spiderman_morales', 'spiderman_movie', 'spiderman_stealth', 'spiderman_black', 'spiderman_2099', 'squirrelgirl', 'starlord', 'storm', 'storm_realm', 'stryfe', 'sunspot', 'skrull_super', 'ironman_superior', 'symbiotesupreme', 'taskmaster', 'terrax', 'thanos', 'champion', 'hood', 'maestro_overseer', 'thing', 'thor', 'thor_janefoster', 'thor_ragnarok', 'tigra', 'toad', 'ultron', 'ultron_prime', 'colossus_unstoppable', 'venom', 'venomtheduck', 'venompool', 'vision', 'vision_timely', 'vision_movie', 'void', 'vulture_movie', 'warmachine', 'warlock', 'wasp', 'wintersoldier', 'wolverine', 'wolverine_weaponx', 'x23', 'yellowjacket', 'yondu']
        return champs_list

    def fancy_to_standard(self, champname):
        standard_champs_list = ['abomination', 'abomination_immortal', 'aegon', 'agentvenom', 'airwalker', 'americachavez', 'angela', 'annihilus', 'antman', 'antivenom', 'apocalypse', 'archangel', 'beast', 'bishop', 'blackbolt', 'blackpanther', 'blackpanther_cw', 'blackwidow', 'blackwidow_timely', 'blackwidow_movie', 'blade', 'cable', 'captainamerica', 'captainamerica_movie', 'captainamerica_samwilson' ,'captainamerica_ww2', 'captainmarvel_movie', 'captainmarvel', 'carnage', 'civilwarrior', 'colossus', 'corvusglaive', 'ghostrider_cosmic', 'crossbones', 'cullobsidian', 'cyclops_90s', 'cyclops', 'daredevil', 'daredevil_netflix', 'darkhawk', 'deadpool', 'deadpool_xforce', 'diablo', 'doctordoom', 'doc_ock', 'drstrange', 'brothervoodoo', 'domino', 'dormammu', 'dragonman', 'drax', 'ebonymaw', 'electro', 'elektra', 'elsabloodstone', 'emmafrost', 'falcon', 'gambit', 'gamora', 'ghost', 'ghostrider', 'deadpool_gold', 'green_goblin', 'groot', 'guardian', 'guillotine', 'guillotine_2099', 'gwenpool', 'havok', 'hawkeye', 'heimdall', 'hela', 'hercules', 'hitmonkey', 'howardmech', 'hulk', 'hulk_immortal', 'hulk_ragnarok', 'hulkbuster_movie', 'humantorch', 'hyperion', 'iceman', 'ikaris', 'invisiblewoman', 'ironfist', 'ironfist_white', 'ironman', 'ironman_movie', 'ironpatriot', 'blackpanther_realm', 'joefixit', 'jubilee', 'juggernaut', 'kang', 'karnak', 'killmonger', 'groot_king', 'kingpin', 'kittypryde', 'knull', 'korg', 'kraven', 'loki', 'longshot', 'lukecage', 'mistyknight' ,'modok', 'magik', 'magneto', 'magneto_marvelnow', 'manthing', 'mangog', 'masacre', 'medusa', 'mephisto', 'mrfantastic', 'misternegative', 'mistersinister', 'mojo', 'moleman', 'moonknight', 'karlmordo', 'morningstar', 'msmarvel', 'msmarvel_kamala', 'mysterio', 'namor', 'nebula', 'nickfury', 'nightthrasher', 'nightcrawler', 'nimrod', 'nova', 'odin', 'wolverine_oldman', 'omegared', 'peniparker', 'phoenix', 'deadpool_platinum', 'professorx', 'proximamidnight', 'psychoman', 'psylocke', 'punisher', 'punisher_2099', 'purgatory', 'quake', 'red_goblin', 'redguardian', 'hulk_red', 'redskull', 'rhino', 'rocket', 'rogue', 'ronan', 'ronin', 'sabretooth', 'sasquatch', 'sauron', 'scarletwitch_current', 'scarletwitch', 'sentinel', 'sentry', 'sersi', 'shangchi', 'shehulk', 'ironman_silvercenturion', 'silversurfer', 'drstrange_realm', 'spidergwen', 'spiderham', 'spiderman', 'spiderman_morales', 'spiderman_movie', 'spiderman_stealth', 'spiderman_black', 'spiderman_2099', 'squirrelgirl', 'starlord', 'storm', 'storm_realm', 'stryfe', 'sunspot', 'skrull_super', 'ironman_superior', 'symbiotesupreme', 'taskmaster', 'terrax', 'thanos', 'champion', 'hood', 'maestro_overseer', 'thing', 'thor', 'thor_janefoster', 'thor_ragnarok', 'tigra', 'toad', 'ultron', 'ultron_prime', 'colossus_unstoppable', 'venom', 'venomtheduck', 'venompool', 'vision', 'vision_timely', 'vision_movie', 'void', 'vulture_movie', 'warmachine', 'warlock', 'wasp', 'wintersoldier', 'wolverine', 'wolverine_weaponx', 'x23', 'yellowjacket', 'yondu']
        fancy_champs_list = ['ABOMINATION', 'ABOMINATION (IMMORTAL)', 'ÆGON', 'AGENT VENOM', 'AIR-WALKER', 'AMERICA CHAVEZ', 'ANGELA', 'ANNIHILUS', 'ANT-MAN', 'ANTI-VENOM', 'APOCALYPSE', 'ARCHANGEL', 'BEAST', 'BISHOP', 'BLACK BOLT', 'BLACK PANTHER', 'BLACK PANTHER (CIVIL WAR)', 'BLACK WIDOW', 'BLACK WIDOW (CLAIRE VOYANT)', 'BLACK WIDOW (DEADLY ORIGIN)', 'BLADE', 'CABLE', 'CAPTAIN AMERICA', 'CAPTAIN AMERICA (INFINITY WAR)', 'CAPTAIN AMERICA (SAM WILSON)', 'CAPTAIN AMERICA (WWII)', 'CAPTAIN MARVEL', 'CAPTAIN MARVEL (CLASSIC)', 'CARNAGE', 'CIVIL WARRIOR', 'COLOSSUS', 'CORVUS GLAIVE', 'COSMIC GHOST RIDER', 'CROSSBONES', 'CULL OBSIDIAN', 'CYCLOPS (BLUE TEAM)', 'CYCLOPS (NEW XAVIER SCHOOL)', 'DAREDEVIL (CLASSIC)', "DAREDEVIL (HELL'S KITCHEN)", 'DARKHAWK', 'DEADPOOL', 'DEADPOOL (X-FORCE)', 'DIABLO', 'DOCTOR DOOM', 'DOCTOR OCTOPUS', 'DOCTOR STRANGE', 'DOCTOR VOODOO', 'DOMINO', 'DORMAMMU', 'DRAGON MAN', 'DRAX', 'EBONY MAW', 'ELECTRO', 'ELEKTRA', 'ELSA BLOODSTONE', 'EMMA FROST', 'FALCON', 'GAMBIT', 'GAMORA', 'GHOST', 'GHOST RIDER', 'GOLDPOOL', 'GREEN GOBLIN', 'GROOT', 'GUARDIAN', 'GUILLOTINE', 'GUILLOTINE 2099', 'GWENPOOL', 'HAVOK', 'HAWKEYE', 'HEIMDALL', 'HELA', 'HERCULES', 'HIT-MONKEY', 'HOWARD THE DUCK', 'HULK', 'HULK (IMMORTAL)', 'HULK (RAGNAROK)', 'HULKBUSTER', 'HUMAN TORCH', 'HYPERION', 'ICEMAN', 'IKARIS', 'INVISIBLE WOMAN', 'IRON FIST', 'IRON FIST (IMMORTAL)', 'IRON MAN', 'IRON MAN (INFINITY WAR)', 'IRON PATRIOT', 'JABARI PANTHER', 'JOE FIXIT', 'JUBILEE', 'JUGGERNAUT', 'KANG', 'KARNAK', 'KILLMONGER', 'KING GROOT', 'KINGPIN', 'KITTY PRYDE', 'KNULL', 'KORG', 'KRAVEN', 'LOKI', 'LONGSHOT', 'LUKE CAGE', 'MISTY KNIGHT', 'M.O.D.O.K.', 'MAGIK', 'MAGNETO', 'MAGNETO (HOUSE OF X)', 'MAN-THING', 'MANGOG', 'MASACRE', 'MEDUSA', 'MEPHISTO', 'MISTER FANTASTIC', 'MISTER NEGATIVE', 'MISTER SINISTER', 'MOJO', 'MOLE MAN', 'MOON KNIGHT', 'MORDO', 'MORNINGSTAR', 'MS. MARVEL', 'MS. MARVEL (KAMALA KHAN)', 'MYSTERIO', 'NAMOR', 'NEBULA', 'NICK FURY', 'NIGHT THRASHER', 'NIGHTCRAWLER', 'NIMROD', 'NOVA', 'ODIN', 'OLD MAN LOGAN', 'OMEGA RED', 'PENI PARKER', 'PHOENIX', 'PLATINUMPOOL', 'PROFESSOR X', 'PROXIMA MIDNIGHT', 'PSYCHO-MAN', 'PSYLOCKE', 'PUNISHER', 'PUNISHER 2099', 'PURGATORY', 'QUAKE', 'RED GOBLIN', 'RED GUARDIAN', 'RED HULK', 'RED SKULL', 'RHINO', 'ROCKET RACCOON', 'ROGUE', 'RONAN', 'RONIN', 'SABRETOOTH', 'SASQUATCH', 'SAURON', 'SCARLET WITCH', 'SCARLET WITCH (CLASSIC)', 'SENTINEL', 'SENTRY', 'SERSI', 'SHANG-CHI', 'SHE-HULK', 'SILVER CENTURION', 'SILVER SURFER', 'SORCERER SUPREME', 'SPIDER-GWEN', 'SPIDER-HAM', 'SPIDER-MAN (CLASSIC)', 'SPIDER-MAN (MILES MORALES)', 'SPIDER-MAN (STARK ENHANCED)', 'SPIDER-MAN (STEALTH SUIT)', 'SPIDER-MAN (SYMBIOTE)', 'SPIDER-MAN 2099', 'SQUIRREL GIRL', 'STAR-LORD', 'STORM', 'STORM (PYRAMID X)', 'STRYFE', 'SUNSPOT', 'SUPER-SKRULL', 'SUPERIOR IRON MAN', 'SYMBIOTE SUPREME', 'TASKMASTER', 'TERRAX', 'THANOS', 'THE CHAMPION', 'THE HOOD', 'THE OVERSEER', 'THING', 'THOR', 'THOR (JANE FOSTER)', 'THOR (RAGNAROK)', 'TIGRA', 'TOAD', 'ULTRON', 'ULTRON', 'UNSTOPPABLE COLOSSUS', 'VENOM', 'VENOM THE DUCK', 'VENOMPOOL', 'VISION', 'VISION (AARKUS)', 'VISION (AGE OF ULTRON)', 'VOID', 'VULTURE', 'WAR MACHINE', 'WARLOCK', 'WASP', 'WINTER SOLDIER', 'WOLVERINE', 'WOLVERINE (WEAPON X)', 'WOLVERINE (X-23)', 'YELLOWJACKET', 'YONDU']
        try:
            fancy_index = fancy_champs_list.index(champname)
            standard_name = standard_champs_list[fancy_index]
            return standard_name
        except:
            return None    

    def add_champ(self,champname, tier:int, rank:int, signature:int, user):
        self.db = self.cluster["MCOC"]["Account"]  
        infodb = self.cluster['MCOC']['Champs']
        discord_id = self.id
        player_check = self.db.find_one({"discord_id":int(discord_id)}, {'_id': 0}) 
        champ_details = infodb.find_one({'champid':champname}, {'_id': 0})
        create_new = True  
        if player_check is not None:
            error = True
            if tier == 6:
                if signature >200:
                    self.error = 'Signature for a 6 star should not be above than 200.'                            
                elif rank >4:
                    self.error = 'Rank of a 6 star should not be above than 4.'
                else:
                    error = False   

            elif tier == 5: 
                if signature >200:
                    self.error = 'Signature for a 5 star should not be above than 200.'
                elif rank >5:
                    self.error = 'Rank of a 5 star should not be above than 5.'
                else:
                    error = False   
        
            elif tier == 4:
                if signature >99:
                    self.error = 'Signature for a 4 star should not be above than 99.'
                elif rank >5:
                    self.error = 'Rank of a 4 star should not be above than 5.'                    
                else:
                    error = False   
                    
            elif tier == 3:
                if signature >99:
                    self.error = 'Signature for a 3 star should not be above than 99.'
                elif rank >4:
                    self.error = 'Rank of a 3 star should not be above than 4.'     
                else:
                    error = False   

            elif tier == 2: 
                if signature >99:
                    self.error = 'Signature for a 2 star should not be above than 99.'
                elif rank >3:
                    self.error = 'Rank of a 2 star should not be above than 3.'         
                else:
                    error = False   

            elif tier == 1:
                self.error = '1 star champs are not supported.'    

            if error == False:
                for roster_dict in player_check['roster']:                
                    if roster_dict['champ_name'] == champ_details['data'][f'{tier}+{rank}']['name'] and roster_dict['tier'] == int(tier):
                        create_new = False                        
                        break
            else:
                pass        
                
            if champ_details is not None:
                if create_new == True:
                    error = True
                    if tier == 6:
                        if signature >200:
                            self.error = 'Signature for a 6 star should not be above than 200.'                            
                        elif rank >4:
                            self.error = 'Rank of a 6 star should not be above than 4.'
                        else:
                            error = False   

                    elif tier == 5: 
                        if signature >200:
                            self.error = 'Signature for a 5 star should not be above than 200.'
                        elif rank >5:
                            self.error = 'Rank of a 5 star should not be above than 5.'
                        else:
                            error = False   
                
                    elif tier == 4:
                        if signature >99:
                            self.error = 'Signature for a 4 star should not be above than 99.'
                        elif rank >5:
                            self.error = 'Rank of a 4 star should not be above than 5.'                    
                        else:
                            error = False   
                            
                    elif tier == 3:
                        if signature >99:
                            self.error = 'Signature for a 3 star should not be above than 99.'
                        elif rank >4:
                            self.error = 'Rank of a 3 star should not be above than 4.'     
                        else:
                            error = False   
    
                    elif tier == 2: 
                        if signature >99:
                            self.error = 'Signature for a 2 star should not be above than 99.'
                        elif rank >3:
                            self.error = 'Rank of a 2 star should not be above than 3.'         
                        else:
                            error = False   
    
                    elif tier == 1:
                        self.error = '1 star champs are not supported.'                         
    
                    if error == False:                                         
                        champ_info = {
                            'champ_name':champ_details['data'][f'{tier}+{rank}']['name'],
                            'tier': tier,
                            'rank': rank,
                            'prestige':int(champ_details['data'][f'{tier}+{rank}']['prestige']),
                            'sig_number':signature,
                            'img_link':champ_details['data'][f'{tier}+{rank}']['img_potrait'],
                            'champid':f'{champ_details["champid"]}+{signature}+{tier}+{rank}',
                            'url_page':champ_details['data'][f'{tier}+{rank}']['url_page']
                        }
                        player_check['roster'].append(champ_info)
                        prestige = 0
                        prestige_list = []
                        for user_dict in player_check['roster']:
                            prestige_list.append(user_dict['prestige'])
                        for prestige_in_dict in prestige_list:
                            prestige = prestige+prestige_in_dict
                        prestige = prestige/len(prestige_list)  
                        player_check['prestige'] = prestige     
                        player_check['avatar_url'] = user.avatar_url
                        player_check['roster'] = sorted(player_check['roster'], key=itemgetter('prestige'), reverse=True)
                        self.db.find_one_and_replace({"discord_id":discord_id}, player_check)
                        self.details = f"Added {tier} star {champ_details['data'][f'{tier}+{rank}']['name']} of rank {rank}, tier {tier} and signature {signature}"
                    else:
                        pass
                else:
                    #Updates the signature, rank and champid
                    for roster_dict in player_check['roster']:
                        if roster_dict['champ_name'] == champ_details['data'][f'{tier}+{rank}']['name'] and roster_dict['tier'] == int(tier): 
                            self.details = f"Updated {tier} star {champ_details['data'][f'{tier}+{rank}']['name']} of previous signature {roster_dict['sig_number']} to new signature {signature} and previous rank {roster_dict['rank']} to new rank {rank}"
                            roster_dict['sig_number'] = signature
                            roster_dict['rank'] = rank
                            roster_dict['champid'] = f'{champ_details["champid"]}+{signature}+{tier}+{rank}'
                            break  
                        prestige = 0 
                        prestige_list = []
                        for user_dict in player_check['roster']:
                            prestige_list.append(user_dict['prestige'])
                        for prestige_in_dict in prestige_list:
                            prestige = prestige+prestige_in_dict
                        prestige = prestige/len(prestige_list)  
                        player_check['prestige'] = prestige   
                        player_check['avatar_url'] = user.avatar_url 
                        player_check['roster'] = sorted(player_check['roster'], key=itemgetter('prestige'), reverse=True)                           
                    self.db.find_one_and_replace({"discord_id":discord_id}, player_check) 
                    self.details = f"Updated {tier} star {champ_details['data'][f'{tier}+{rank}']['name']}. "                        
            else:
                self.error = 'Champname is incorrect. Refer to https://github.com/Rexians/uma/blob/master/champnames.md for correct champnames.'    
        else:
            self.error = 'Player with this name doesn\'t exists.'                                  

    def get_users_data(self):
        documents = self.db.find({}, {'_id': 0})
        user_list = []
        for document in documents:
            user_list.append(document)
        return user_list

    def get_users_advanced_data(self):
        documents = self.db.find({}, {'_id': 0})
        users_dict = {}
        for document in documents:
            users_dict[document['discord_id']] = document
        return users_dict    

    def get_ids(self):
        documents = self.db.find({}, {'_id': 0})
        ids_list = []
        for document in documents:
            user_id = document['discord_id']
            ids_list.append(user_id)
        return ids_list            

    def add_ally_token(self, ally_token):
        user_acc = self.user_acc
        user_acc['alliance'] = ally_token
        change = self.db.find_one_and_replace({'discord_id':self.id}, user_acc)
        if change is None:
            return False
        else:
            return True    

    def leave_ally(self):
        user_acc = self.user_acc
        user_acc['alliance'] = None
        try:
            self.db.find_one_and_replace({'discord_id':self.id}, user_acc)
            return True
        except:
            return False    

class AllianceDataBase():
    '''
    Used to access the Allinace DataBase.
    '''
    def __init__(self) -> None:
        cluster = os.environ.get('CLUSTER')
        client = MongoClient(cluster)
        db = client['MCOC']['Alliance']
        self.db = db

    def create_ally(self, ally_name, ally_tag, ally_token, date, leader_profile:dict):
        prev_ally = self.db.find_one({"ally_name":ally_name, "ally_tag":ally_tag, "ally_token":ally_token}, {'_id':0})
        if prev_ally is None:
            data = {
                "ally_name":ally_name,
                "ally_tag":ally_tag,
                "ally_token":ally_token,
                "members":{
                    'leader':leader_profile, 
                    'officers':[], 
                    'members':[]
                    },
                "date_created":date}

            self.db.insert_one(data)
            return True #Ally doesn't exists, So created.
        else:
            return False #Ally exists.

    def get_details(self, ally_token): 
        data = self.db.find_one({'ally_token':ally_token}, {'_id':0})
        if data is not None:
            return data
        else:
            return False    

    def add_member(self, ally_token, member_profile:dict):       
        ally = self.db.find_one({"ally_token":ally_token}, {'_id':0})
        if ally is not None:
            ally['members']['members'].append(member_profile)
            self.db.find_one_and_replace({"ally_token":ally_token}, ally)
            return True
        else:
            return False #Ally token invalid/Ally doesn't exist! 

    def add_officer(self, ally_token, officer_profile:dict):       
        ally = self.db.find_one({"ally_token":ally_token}, {'_id':0})
        if ally is not None:
            ally['members']['officers'].append(officer_profile)
            self.db.find_one_and_replace({"ally_token":ally_token}, ally)
            return True
        else:
            return False #Ally token invalid/Ally doesn't exist!

