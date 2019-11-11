# Utilities For Nexxy

DAMAGE_TYPE = ('fire', 'cold', 'acid', 'shock', 'sonic', 'holy', 'unholy', 'negative', 'positive', 'untyped', 'poison', 'piercing', 'bludgeoning', 'slashing', 'law', 'chaos')
RESIST_TYPE = ('immune', 'vulnerable', 'resist', 'neutral')
SAVE_TYPE = ('fortitudeSave', 'reflexSave', 'willSave')

ATTRIBUTE_NAMES = ('strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma')

ATTRIBUTE_ABBREVIATIONS = ('str', 'dex', 'con', 'int', 'wis', 'cha')

SKILL_IDS = ('acrobatics', 'appraise', 'bluff', 'climb', 'craft', 'diplomacy', 'disableDevice', 'fly', 'handleAnimal', 'heal', 'intimidate', 'kArcana', 'kDungeoneering', 
			'kEngineering', 'kGeography', 'kHistory', 'kLocal', 'kNature', 'kNobility', 'kPlanes', 'kReligion', 'linguistics', 'perception', 'perform', 'profession', 'ride', 'senseMotive', 'sleightOfHand',
			'spellcraft', 'stealth', 'survival', 'swim', 'useMagicDevice')

SAVE_BONUSES = ('strengthSave', 'dexteritySave', 'constitutionSave', 'intelligenceSave', 'wisdomSave', 'charismaSave')

SKILL_MAP = {
            'fortitudeSave': 'constitution',
			'reflexSave': 'dexterity',
			'willSave': 'wisdom',
			'acrobatics': 'dexterity', 
			'appraise': 'intelligence',
			'bluff': 'charisma', 
			'climb': 'strength', 
			'craft': 'intelligence', 
			'diplomacy': 'charisma', 
			'disableDevice': 'dexterity', 
			'fly': 'dexterity', 
			'handleAnimal': 'charisma', 
			'heal': 'wisdom', 
			'intimidate': 'charisma', 
			'kArcana': 'intelligence', 
			'kDungeoneering': 'intelligence', 
			'kEngineering': 'intelligence', 
			'kGeography': 'intelligence', 
			'kHistory': 'intelligence', 
			'kLocal': 'intelligence', 
			'kNature': 'intelligence', 
			'kNobility': 'intelligence', 
			'kPlanes': 'intelligence', 
			'kReligion': 'intelligence', 
			'linguistics': 'intelligence', 
			'perception': 'wisdom', 
			'perform': 'charisma', 
			'profession':'wisdom', 
			'ride': 'dexterity', 
			'senseMotive': 'wisdom', 
			'sleightOfHand': 'dexterity', 
			'spellcraft': 'intelligence', 
			'stealth': 'dexterity', 
			'survival': 'wisdom', 
			'swim': 'strength', 
			'useMagicDevice': 'charisma',
			'strengthSave': 'strength', 
			'dexteritySave': 'dexterity', 
			'constitutionSave': 'constitution', 
			'intelligenceSave': 'intelligence',
			'wisdomSave': 'wisdom', 
			'charismaSave': 'charisma'
}

SKILL_CRAFT_SELECTION = ('alchemy', 'armor', 'baskets', 'books', 'bows', 'calligraphy', 'carpentry', 'cloth', 
							'clothing', 'glass', 'jewelry', 'leather', 'locks', 'paintings', 'pottery', 'sculptures',
							 'ships', 'shoes', 'stonemasonry', 'traps', 'weapons', 'other'
	)
SKILL_PERFORM_SELECTION = ('act', 'comedy', 'dance', 'keyboard', 'oratory', 'percussion', 'stringInstruments', 'windInstruments', 'sing'
	)