from Items.Materials.golagtatite import golagtatite
from Items.Materials.wolf_pelt import wolf_pelt
from Utility.colors import colors


class golagtatite_shoes:

    # every equipment piece has all the power to change any stat
    # think of items as stat sticks, change the stats here
    dmg = 0
    crc = 0.0
    hp = 3
    speed = -1
    armor = 3

    # keep as decimals
    armor_percent = 0.0
    xp_bonus = 0.0
    fire_resistance = 0.02
    shock_resistance = 0.01
    poison_amp = 0.0

    type = "boots"

    # if this item is craftable, what do you need to craft it? craftable items must be added to crafting.py
    # recipe is a dictionary, use this format:
    # MATERIAL: AMOUNT
    recipe = {golagtatite: 4, wolf_pelt: 2}

    # SET TO NONE IF YOU DO NOT WANT IT TO BE SELLABLE
    sell = 35

    # set buying price, must add item to respective kingdom's shop market
    buy = 0

    # what level do you need to be to equip this item?
    lvl_req = 0

    name = f"{colors.LightGreen}Golagtatite Shoes{colors.Reset}"

    # ADD ALL VARIABLES CHANGED TO DESCRIPTION
    desc = f"Made from almost pure Golagtatite, these will protect you decently, at the sacrifice of speed." \
           f"\n{colors.Cyan}LVL REQUIRED: {colors.LightCyan}{lvl_req}{colors.Reset}" \
           f"\n{colors.Green}HP: {colors.LightGreen}{hp}" \
           f"\n{colors.White}Speed: {speed}" \
           f"\n{colors.Yellow}Armor: {colors.LightYellow}{armor}" \
           f"\n{colors.LightRed}Fire Res: {fire_resistance * 100}%" \
           f"\n{colors.LightYellow}Shock Res: {shock_resistance * 100}%{colors.Reset}" \
           f"\n{colors.LightGreen}Sell Price: {colors.Green}${sell}{colors.Reset}"

    def __init__(self):
        pass

    # used if item is craftable, do not delete
    @staticmethod
    def print_recipe():
        string = ""
        for key in golagtatite_shoes.recipe:
            string = f"{string}| {golagtatite_shoes.recipe[key]}x {key.name} | "

        return string

