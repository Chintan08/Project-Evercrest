from Utility.colors import colors


class no_accessory:

    # every equipment piece has all the power to change any stat
    dmg = 0.0
    crc = 0.0
    hp = 0.0
    speed = 0.0
    armor = 0.0
    armor_percent = 0.0
    immune_to_burn = False

    type = "accessory"

    discovered = False

    recipe = {}
    sell = 12.5
    buy = 25.0

    lvl_req = 0

    name = f"{colors.White}No Accessory{colors.Reset}"
    desc = f"You seemingly have no accessory on." \

    def __init__(self):
        pass