from Utility.colors import colors


class shoes:

    # every equipment piece has all the power to change any stat
    dmg = 0.0
    crc = 0.0
    hp = 0.0
    speed = 0.0
    armor = 0.0
    armor_percent = 0.0
    immune_to_burn = False

    type = "boots"

    discovered = False

    recipe = {}
    sell = 12.5
    buy = 25.0

    lvl_req = 0

    name = f"{colors.White}Shoes{colors.Reset}"
    desc = f"Nice shoes." \
           f"\n{colors.Red}ARMOR{colors.Reset}: {colors.LightRed}{armor}{colors.Reset} " \
           f"\n{colors.Magenta}ARMOR%{colors.Reset}: {colors.LightMagenta}{armor_percent}{colors.Reset}"

    def __init__(self):
        pass