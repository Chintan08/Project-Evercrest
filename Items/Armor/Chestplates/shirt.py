from Utility.colors import colors


class shirt(object):

    # every equipment piece has all the power to change any stat
    dmg = 0.0
    crc = 0.0
    hp = 0.0
    speed = 0.0
    armor = 0.0
    armor_percent = 0.0
    xp_bonus = 0.0
    fire_resistance = 0.0
    shock_resistance = 0.0
    poison_amp = 0.0

    type = "chestplate"

    recipe = {}
    sell = 12.5
    buy = 25.0

    lvl_req = 0

    name = f"{colors.White}Shirt{colors.Reset}"
    desc = f"Shirts don't help." \
           f"\n{colors.Red}ARMOR{colors.Reset}: {colors.LightRed}{armor}{colors.Reset} " \
           f"\n{colors.Magenta}ARMOR%{colors.Reset}: {colors.LightMagenta}{armor_percent}{colors.Reset}"

    def __init__(self):
        pass