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

class Character:
    def __init__(self, name, faction, character_class, level, stats, equipment, inventory):
        self.name = name
        self.faction = faction
        self.character_class = character_class

# Example usage
stats = Stats(strength=10, dexterity=8, intelligence=7, vitality=9)
equipment = Equipment(weapon="Sword", armor="Chainmail", accessory="Ring of Strength")
inventory = Inventory(items=["Potion", "Elixir"], gold=100)

character = Character(
    name="Aragorn",
    faction="Human",
    character_class="Warrior",
    level=5,
    stats=stats,
    equipment=equipment,
    inventory=inventory
)

print(character.__dict__)

class CharacterClassInfo:
    def __init__(self):
        self.classes = {
            "Tank": {
                "class_name": "Tank",
                "starting_stats": Stats(strength=12, dexterity=4, intelligence=3, vitality=10),
                "starting_equipment": Equipment(weapon="Common Shield", armor="Common Plate Armor", accessory="Common Amulet of Protection"),
                "starting_level": 1,
                "starting_experience": 0
            },
            "Warrior": {
                "class_name": "Warrior",
                "starting_stats": Stats(strength=10, dexterity=5, intelligence=3, vitality=8),
                "starting_equipment": Equipment(weapon="Common Sword", armor="Common Chainmail", accessory="Common Ring of Strength"),
                "starting_level": 1,
                "starting_experience": 0
            },
            "Mage": {
                "class_name": "Mage",
                "starting_stats": Stats(strength=3, dexterity=5, intelligence=10, vitality=4),
                "starting_equipment": Equipment(weapon="Common Staff", armor="Common Robe", accessory="Common Amulet of Wisdom"),
                "starting_level": 1,
                "starting_experience": 0
            },
            "Rogue": {
                "class_name": "Rogue",
                "starting_stats": Stats(strength=6, dexterity=10, intelligence=4, vitality=5),
                "starting_equipment": Equipment(weapon="Common Dagger", armor="Common Leather Armor", accessory="Common Cloak of Shadows"),
                "starting_level": 1,
                "starting_experience": 0
            },
            "Hunter": {
                "class_name": "Hunter",
                "starting_stats": Stats(strength=7, dexterity=8, intelligence=5, vitality=6),
                "starting_equipment": Equipment(weapon="Common Bow", armor="Common Leather Armor", accessory="Common Quiver of Arrows"),
                "starting_level": 1,
                "starting_experience": 0
            },
        }

    def get_class_info(self, class_name):
        return self.classes.get(class_name, None)
    
# Example usage
class_info = CharacterClassInfo()
warrior_info = class_info.get_class_info("Warrior")
print(warrior_info)