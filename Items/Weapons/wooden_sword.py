from Utility.colors import colors
from Items.Materials.golagtatite import golagtatite

class wooden_sword(object):

    # every equipment piece has all the power to change any stat
    dmg = 7.0
    crc = .025
    hp = 0.0
    speed = 0.0
    armor = 0.0
    armor_percent = 0.0
    xp_bonus = 0.0
    fire_resistance = 0.0
    shock_resistance = 0.0
    poison_amp = 0.0

    type = "weapon"
    wclass = "sword"

    recipe = {}

    sell = 20.0
    buy = 40.0

    lvl_req = 0

    name = f"{colors.White}Wooden Sword{colors.Reset}"
    desc = f"A simple wooden sword, made with no effort, and it shows. " \
           f"\n{colors.Cyan}LVL REQUIRED: {colors.LightCyan}{lvl_req}{colors.Reset}" \
           f"\n{colors.Cyan}Weapon Class: {colors.LightCyan}{wclass.upper()}{colors.Reset}" \
           f"\n{colors.Red}Damage: {colors.LightRed}{dmg}{colors.Reset} " \
           f"\n{colors.Magenta}CRIT%: {colors.LightMagenta}{crc}{colors.Reset}" \
           f"\n{colors.LightGreen}Sell Price: ${sell}{colors.Reset}"

    def __init__(self):
        pass

    @staticmethod
    def print_recipe():
        string = ""
        for key in wooden_sword.recipe:
            string = f"{string}| {wooden_sword.recipe[key]}x {key.name} | "

        return string

    @staticmethod
    def return_item():
        return "wooden_sword"
