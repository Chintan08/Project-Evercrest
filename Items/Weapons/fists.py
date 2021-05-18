from Utility.colors import colors

class fists:

    # every equipment piece has all the power to change any stat
    dmg = 0.0
    crc = 0.0
    hp = 0.0
    speed = 0.0
    armor = 0.0
    armor_percent = 0.0
    immune_to_burn = False

    type = "weapon"
    wclass = "brawling"

    discovered = False

    recipe = {}
    sell = 12.5
    buy = 25.0

    lvl_req = 0

    name = f"{colors.White}Fists{colors.Reset}"
    desc = f"Your Fists... how did you discover your fists?" \
           f"\n{colors.Red}ATK{colors.Reset}: {colors.LightRed}{dmg}{colors.Reset} " \
           f"\n{colors.Magenta}CRIT%{colors.Reset}: {colors.LightMagenta}{crc}{colors.Reset}"

    def __init__(self):
        pass

