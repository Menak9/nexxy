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