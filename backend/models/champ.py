from dataclasses import dataclass

@dataclass
class Champ:
    "Class for creating a champ"
    champ_id: str
    champ_name: str
    champ_class: str
    tier: int
    rank: int
    prestige: int
    champ_img: str
    sig: int = 0
    level: int = 0

    def create_champ(self) -> dict:
        return {"champ_id": self.champ_id,
                "champ_name": self.champ_name,
                "champ_class": self.champ_class,
                "sig": self.sig,
                "level": self.level,
                "tier": self.tier,
                "rank": self.rank,
                "prestige": self.prestige,
                "champ_img": self.champ_img}
