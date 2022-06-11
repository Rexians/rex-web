def convert(champ_url):
    champ_urls = {
        "blackwidow_timely": "bwcv",
        "red_goblin": "redgoblin",
        "blackwidow_movie": "bwdo",
        "ultron_prime": "ultron",
        "ultron": "ultronlol",
        "spiderman_black": "spidersymbiote",
        "karlmordo": "mordo",
        "drstrange_realm": "sorcerersupreme",
        "wolverine_oldman": "oml",
        "hulkbuster_movie": "hulkbuster",
        "ironfist_white": "ironfistimmortal",
        "cyclops_90s": "cyclops_blue",
        "captainmarvel_movie": "cmm",
        "captainamerica_movie": "caiw",
        "captainamerica_samwilson": "casw",
        "captainamerica_ww2": "caww2",
        "ironman_movie": "imiw",
        "blackpanther_realm": "jabaripanther",
        "groot_king": "kinggroot",
        "mrfantastic": "misterfantastic",
        "blackpanther_cw": "bpcw",
        "punisher_2099": "punisher2099",
        "rocket": "rocketracoon",
        "spiderman_2099": "spiderman2099",
        "maestro_overseer": "overseer",
        "colossus_unstoppable": "unstoppablecolossus",
        "vision_timely": "visionaarkus",
        "vision_movie": "visionmovie",
        "vulture_movie": "vulture",
        "wolverine_weaponx": "wolverinex",
        "spiderman_morales": "spidermorales",
        "spiderman_movie": "starkspiderman",
        "spiderman_stealth": "spiderstealth",
        "magneto": "redmagneto",
        "magneto_marvelnow": "magnetowhite",
        "msmarvel_kamala": "kamalakhan",
        "deadpool_platinumpool": "platinumpool",
        "scarletwitch_current": "scarletwitchnew",
        "ironman_silvercenturion": "silvercenturion",
        "storm_realm": "stormpyramidx",
        "skrull_super": "superskrull",
        "ironman_superior": "superiorironman",
        "thor_janefoster": "janefoster",
        "thor_ragnarok": "thorragnarok",
        "abomination_immortal": "ibom",
        "brothervoodoo": "doctorvoodoo",
        "daredevil_netflix": "daredevil netflix",
        "deadpool_goldpool": "goldpool",
        "ghostrider_cosmic": "cgr",
        "doc_ock": "docock",
        "green_goblin": "greengoblin",
        "howardmech": "howard"
    }

    try:
        new = champ_urls[champ_url]
        return new
    except KeyError:
        return champ_url