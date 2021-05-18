from Utility.colors import colors


class stronias_heirloom:

    # every equipment piece has all the power to change any stat
    dmg = 150.0
    crc = 0.0
    hp = 0.0
    speed = -1.0
    armor = 5.0
    armor_percent = 0.0
    immune_to_burn = False

    type = "weapon"
    wclass = "sword"

    discovered = False

    recipe = {}

    sell = 0
    buy = 0

    lvl_req = 0

    name = f"{colors.LightRed}Stronia's Heirloom{colors.Reset}"
    desc = f"The epic hammer Prida Stronia wielded. Do not get in the swing's way. " \
           f"\n{colors.Red}ATK{colors.Reset}: {colors.LightRed}{dmg}{colors.Reset} " \
           f"\n{colors.Magenta}CRIT%{colors.Reset}: {colors.LightMagenta}{crc}{colors.Reset}"

    def __init__(self):
        pass

    @staticmethod
    def print_recipe():
        string = ""
        for key in stronias_heirloom.recipe:
            string = f"{string}| {stronias_heirloom.recipe[key]}x {key.name} | "

        return string

