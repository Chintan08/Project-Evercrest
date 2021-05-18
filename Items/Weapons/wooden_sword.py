from Utility.colors import colors
from Items.Materials.golagtatite import golagtatite

class wooden_sword:

    # every equipment piece has all the power to change any stat
    dmg = 15.0
    crc = .05
    hp = 0.0
    speed = 0.0
    armor = 0.0
    armor_percent = 0.0
    immune_to_burn = False

    type = "weapon"
    wclass = "sword"

    discovered = False

    recipe = {golagtatite: 1}

    sell = 12.5
    buy = 25.0

    lvl_req = 0

    name = f"{colors.White}Wooden Sword{colors.Reset}"
    desc = f"A simple wooden sword, made with no effort, and it shows. " \
           f"\n{colors.Red}ATK{colors.Reset}: {colors.LightRed}{dmg}{colors.Reset} " \
           f"\n{colors.Magenta}CRIT%{colors.Reset}: {colors.LightMagenta}{crc}{colors.Reset}"

    def __init__(self):
        pass

    @staticmethod
    def print_recipe():
        string = ""
        for key in wooden_sword.recipe:
            string = f"{string}| {wooden_sword.recipe[key]}x {key.name} | "

        return string

