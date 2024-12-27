class Character:
    def __init__(self, character_id, name, faction, character_class, stats, equipment, inventory):
        self.character_id = character_id
        self.name = name
        self.faction = faction
        self.character_class = character_class
        self.stats = stats
        self.equipment = equipment
        self.inventory = inventory

class Stats:
    def __init__(self, strength, dexterity, intelligence, vitality):
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.vitality = vitality

class Equipment:
    def __init__(self, weapon, armor, accessory):
        self.weapon = weapon
        self.armor = armor
        self.accessory = accessory

class Inventory:
    def __init__(self, items, gold):
        self.items = items
        self.gold = gold

class CharacterClassInfo:
    def __init__(self):
        self.classes = {
            "Tank": {
                "class_name": "Tank",
                "starting_stats": Stats(strength=12, dexterity=4, intelligence=3, vitality=10),
                "starting_equipment": Equipment(weapon="Common Shield", armor="Common Plate Armor", accessory="Common Amulet of Protection"),
                "starting_inventory": Inventory(items=["Health Potion", "Mana Potion"], gold=50),
                "starting_level": 1,
                "starting_experience": 0
            },
            "Warrior": {
                "class_name": "Warrior",
                "starting_stats": Stats(strength=10, dexterity=5, intelligence=3, vitality=8),
                "starting_equipment": Equipment(weapon="Common Sword", armor="Common Chainmail", accessory="Common Ring of Strength"),
                "starting_inventory": Inventory(items=["Health Potion", "Mana Potion"], gold=50),
                "starting_level": 1,
                "starting_experience": 0
            },
            "Mage": {
                "class_name": "Mage",
                "starting_stats": Stats(strength=3, dexterity=5, intelligence=10, vitality=4),
                "starting_equipment": Equipment(weapon="Common Staff", armor="Common Robe", accessory="Common Amulet of Wisdom"),
                "starting_inventory": Inventory(items=["Health Potion", "Mana Potion"], gold=50),
                "starting_level": 1,
                "starting_experience": 0
            },
            "Rogue": {
                "class_name": "Rogue",
                "starting_stats": Stats(strength=6, dexterity=10, intelligence=4, vitality=5),
                "starting_equipment": Equipment(weapon="Common Dagger", armor="Common Leather Armor", accessory="Common Cloak of Shadows"),
                "starting_inventory": Inventory(items=["Health Potion", "Mana Potion"], gold=50),
                "starting_level": 1,
                "starting_experience": 0
            },
            "Hunter": {
                "class_name": "Hunter",
                "starting_stats": Stats(strength=7, dexterity=8, intelligence=5, vitality=6),
                "starting_equipment": Equipment(weapon="Common Bow", armor="Common Leather Armor", accessory="Common Quiver of Arrows"),
                "starting_inventory": Inventory(items=["Health Potion", "Mana Potion"], gold=50),
                "starting_level": 1,
                "starting_experience": 0
            },
        }

    def get_class_info(self, class_name):
        return self.classes.get(class_name, None)

class CharacterIDGenerator:
    def __init__(self):
        self.current_id = 0

    def get_next_character_id(self):
        self.current_id += 1
        return self.current_id

id_generator = CharacterIDGenerator()
    
# Example usage
class_info = CharacterClassInfo()
warrior_info = class_info.get_class_info("Warrior")
print(warrior_info)

# Example usage
stats = Stats(strength=10, dexterity=8, intelligence=7, vitality=9)
equipment = Equipment(weapon="Sword", armor="Chainmail", accessory="Ring of Strength")
inventory = Inventory(items=["Potion", "Elixir"], gold=100)
character_class = class_info.get_class_info("Warrior")

new_character = Character(
    character_id=id_generator.get_next_character_id(),
    name="Aragorn",
    faction="Human",
    character_class=character_class,
    stats=character_class["starting_stats"],
    equipment=character_class["starting_equipment"],
    inventory=character_class["starting_inventory"]
)

print(f"Character ID: {new_character.character_id}")
print(f"Name: {new_character.name}")
print(f"Faction: {new_character.faction}")
print(f"Class: {new_character.character_class['class_name']}")
print("Stats:")
print(f"  Strength: {new_character.stats.strength}")
print(f"  Dexterity: {new_character.stats.dexterity}")
print(f"  Intelligence: {new_character.stats.intelligence}")
print(f"  Vitality: {new_character.stats.vitality}")
print("Equipment:")
print(f"  Weapon: {new_character.equipment.weapon}")
print(f"  Armor: {new_character.equipment.armor}")
print(f"  Accessory: {new_character.equipment.accessory}")
print("Inventory:")
print(f"  Items: {', '.join(new_character.inventory.items)}")
print(f"  Gold: {new_character.inventory.gold}")
