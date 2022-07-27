from Utility.colors import colors

class bandit_scimitar:

    # every equipment piece has all the power to change any stat
    dmg = 18.0
    crc = .05
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

    sell = None
    buy = 0

    lvl_req = 3

    name = f"{colors.LightBlue}Bandit Scimitar{colors.Reset}"
    desc = f"A scimitar used by the Mountain Vulture Bandit Gang. It deals nice damage, and looks cool. What more can you ask for?" \
           f"\n{colors.Cyan}LVL REQUIRED: {colors.LightCyan}{lvl_req}{colors.Reset}" \
           f"\n{colors.Cyan}Weapon Class: {colors.LightCyan}{wclass.upper()}{colors.Reset}" \
           f"\n{colors.Red}Damage: {colors.LightRed}{dmg}{colors.Reset} " \
           f"\n{colors.Magenta}CRIT%: {colors.LightMagenta}{crc}{colors.Reset}"

    def __init__(self):
        pass

    @staticmethod
    def print_recipe():
        string = ""
        for key in bandit_scimitar.recipe:
            string = f"{string}| {bandit_scimitar.recipe[key]}x {key.name} | "

        return string

