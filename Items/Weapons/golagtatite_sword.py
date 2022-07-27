from Items.Materials.golagtatite import golagtatite
from Items.Materials.snake_fang import snake_fang
from Utility.colors import colors


class golagtatite_sword:
    # every equipment piece has all the power to change any stat
    # think of items as stat sticks, change the stats here
    dmg = 12
    crc = 0.0
    hp = 0.0
    speed = -1
    armor = 1.0

    # keep as decimals
    armor_percent = 0.0
    xp_bonus = 0.0
    fire_resistance = 0.0
    shock_resistance = 0.0
    poison_amp = 0.0

    # DO NOT CHANGE THIS
    type = "weapon"

    # What type of weapon is this? Used in abilities. Keep as a string
    # Types: brawling, sword, hammer, axe, bow
    wclass = "sword"

    # if this item is craftable, what do you need to craft it? craftable items must be added to crafting.py
    # recipe is a dictionary, use this format:
    # MATERIAL: AMOUNT
    recipe = {snake_fang: 4, golagtatite: 4}

    # SET TO NONE IF YOU DO NOT WANT IT TO BE SELLABLE
    sell = 35

    # set buying price, must add item to respective kingdom's shop market
    buy = 0

    # what level do you need to be to equip this item?
    lvl_req = 0

    name = f"{colors.LightGreen}Golagtatite Sword{colors.Reset}"

    # ADD ALL VARIABLES CHANGED TO DESCRIPTION
    desc = f"Forged from Golagtatite, its snake fang blade is sure to cut into your opponents." \
           f"\n{colors.Cyan}LVL REQUIRED: {colors.LightCyan}{lvl_req}{colors.Reset}" \
           f"\n{colors.Cyan}Weapon Class: {colors.LightCyan}{wclass.upper()}{colors.Reset}" \
           f"\n{colors.Red}Damage: {colors.LightRed}{dmg}" \
           f"\n{colors.Yellow}Armor: {colors.LightYellow}{armor}" \
           f"\n{colors.White}Speed: {speed}{colors.Reset}" \
           f"\n{colors.LightGreen}Sell Price: ${sell}{colors.Reset}"

    def __init__(self):
        pass

    # used if item is craftable, do not delete
    @staticmethod
    def print_recipe():
        string = ""
        for key in golagtatite_sword.recipe:
            string = f"{string}| {golagtatite_sword.recipe[key]}x {key.name} | "

        return string


