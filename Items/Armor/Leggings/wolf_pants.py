from Items.Materials.golagtatite import golagtatite
from Items.Materials.wolf_pelt import wolf_pelt
from Utility.colors import colors


class wolf_pants:

    # every equipment piece has all the power to change any stat
    # think of items as stat sticks, change the stats here
    dmg = 0
    crc = 0.02
    hp = 8
    speed = 0
    armor = 1

    # keep as decimals
    armor_percent = 0.0
    xp_bonus = 0.0
    fire_resistance = 0.02
    shock_resistance = 0.01
    poison_amp = 0.0

    type = "helmet"

    # if this item is craftable, what do you need to craft it? craftable items must be added to crafting.py
    # recipe is a dictionary, use this format:
    # MATERIAL: AMOUNT
    recipe = {golagtatite: 2, wolf_pelt: 3}

    # SET TO NONE IF YOU DO NOT WANT IT TO BE SELLABLE
    sell = 35

    # set buying price, must add item to respective kingdom's shop market
    buy = 0

    # what level do you need to be to equip this item?
    lvl_req = 0

    name = f"{colors.LightGreen}Wolf Pants{colors.Reset}"

    # ADD ALL VARIABLES CHANGED TO DESCRIPTION
    desc = f"Made up of mostly Wolf Pelt, these pants will protect you nicely." \
           f"\n{colors.Cyan}LVL REQUIRED: {colors.LightCyan}{lvl_req}{colors.Reset}" \
           f"\n{colors.Green}HP: {colors.LightGreen}{hp}" \
           f"\n{colors.White}Speed: {speed}" \
           f"\n{colors.Yellow}Armor: {colors.LightYellow}{armor}" \
           f"\n{colors.Magenta}CRC: {colors.LightMagenta}{crc}" \
           f"\n{colors.LightRed}Fire Res: {fire_resistance * 100}%" \
           f"\n{colors.LightYellow}Shock Res: {shock_resistance * 100}%{colors.Reset}" \
           f"\n{colors.LightGreen}Sell Price: ${sell}{colors.Reset}"

    def __init__(self):
        pass

    # used if item is craftable, do not delete
    @staticmethod
    def print_recipe():
        string = ""
        for key in wolf_pants.recipe:
            string = f"{string}| {wolf_pants.recipe[key]}x {key.name} | "

        return string

