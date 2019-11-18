# This is where Core Character will be developed. This page will call a character and be used during all parts of creation, 
# though there will be a function section that will handle actions and player movement. This will be the base and core section. 
from utilitesCore import ATTRIBUTE_NAMES, SAVE_TYPE, RESIST_TYPE, ATTRIBUTE_ABBREVIATIONS, SAVE_BONUSES
# from Nexxy/Library import RACE_ATTRIBUTE_MODIFIERS
class BaseStats:
    def __init__(self, base_attack_bonus: int, strength: int, dexterity: int, constitution: int, intelligence: int,
                 wisdom: int, charisma: int):
        self.base_attack_bonus = base_attack_bonus
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return {
            "base_attack_bonus": self.base_attack_bonus, "strength": self.strength, "dexterity": self.dexterity,
            "constitution": self.constitution, "intelligence": self.intelligence, "wisdom": self.wisdom,
            "charisma": self.charisma
        }
    # Functions to call the above elements
    @classmethod
    def default(cls):
        return cls(0, 10, 10, 10, 10, 10, 10)

    def get_mod(self, stat: str):
        attr_short = stat.lower()[:3]
        if attr_short not in ATTRIBUTE_ABBREVIATIONS:
            raise ValueError(f"{stat} is not a valid stat.")
        return {
            'str': self.strength // 2 - 5, 'dex': self.dexterity // 2 - 5,
            'con': self.constitution // 2 - 5, 'int': self.intelligence // 2 - 5,
            'wis': self.wisdom // 2 - 5, 'cha': self.charisma // 2 - 5
        }[attr_short]
    def __str__(self):
        return f"**STR**: {self.strength} ({(self.strength - 10) // 2:+}) " \
               f"**DEX**: {self.dexterity} ({(self.dexterity - 10) // 2:+}) " \
               f"**CON**: {self.constitution} ({(self.constitution - 10) // 2:+})\n" \
               f"**INT**: {self.intelligence} ({(self.intelligence - 10) // 2:+}) " \
               f"**WIS**: {self.wisdom} ({(self.wisdom - 10) // 2:+}) " \
               f"**CHA**: {self.charisma} ({(self.charisma - 10) // 2:+})"
    def __getitem__(self, item):  # Error Catching
        if item not in ATTRIBUTE_NAMES:
            raise ValueError(f"{item} is not a stat.")
        return getattr(self, item)
    
class BaseLevels:
    def __init__(self, classes: dict = None, total_level: int = None):
        if classes is None:
            classes = {}
        self.total_level = total_level or sum(classes.values())
        self.classes = classes