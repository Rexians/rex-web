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

    def create_champ(self) -> dict:
        return {"champ_id": self.champ_id,
                "champ_name": self.champ_name,
                "champ_class": self.champ_class,
                "tier": self.tier,
                "rank": self.rank,
                "prestige": self.prestige}
