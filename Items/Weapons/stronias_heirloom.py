from Utility.colors import colors


class stronias_heirloom:

    # every equipment piece has all the power to change any stat
    dmg = 150.0
    crc = 0.0
    hp = 0.0
    speed = 100
    armor = 5.0
    armor_percent = 0.0
    xp_bonus = 0.0
    fire_resistance = 0.0
    shock_resistance = 0.0
    poison_amp = 0.0

    type = "weapon"
    wclass = "hammer"

    recipe = {}

    sell = None
    buy = 0

    lvl_req = 0

    name = f"{colors.LightRed}Stronia's Heirloom{colors.Reset}"
    desc = f"The epic hammer Prida Stronia wielded. Do not get in the swing's way. " \
           f"\nThis hammer fortifies you, granting you increased armor, but due to its sheer size and weight, it does not hesitate to slow you down." \
           f"\n{colors.Cyan}LVL REQUIRED: {colors.LightCyan}{lvl_req}{colors.Reset}" \
           f"\n{colors.Cyan}Weapon Class: {colors.LightCyan}{wclass.upper()}{colors.Reset}" \
           f"\n{colors.Red}Damage: {colors.LightRed}{dmg}{colors.Reset} " \
           f"\n{colors.White}Speed: {speed}" \
           f"\n{colors.Yellow}Armor: {colors.LightYellow}{armor}{colors.Reset}"

    def __init__(self):
        pass

    @staticmethod
    def print_recipe():
        string = ""
        for key in stronias_heirloom.recipe:
            string = f"{string}| {stronias_heirloom.recipe[key]}x {key.name} | "

        return string

