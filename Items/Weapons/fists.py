from Utility.colors import colors

class fists:

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

    type = "weapon"
    wclass = "brawling"

    recipe = {}
    sell = None
    buy = 0

    lvl_req = 0

    name = f"{colors.White}Fists{colors.Reset}"
    desc = f"Your Fists, the only weapon you need!" \
           f"\n{colors.Cyan}Weapon Class: {colors.LightCyan}{wclass.upper()}{colors.Reset}" \


    def __init__(self):
        pass
