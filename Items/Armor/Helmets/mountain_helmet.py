from Items.Materials.golagtatite import golagtatite
from Items.Materials.wolf_pelt import wolf_pelt
from Utility.colors import colors


class mountain_helmet:

    # every equipment piece has all the power to change any stat
    # think of items as stat sticks, change the stats here
    dmg = 0
    crc = 0.02
    hp = 5
    speed = 1
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

    name = f"{colors.LightGreen}Mountain Helmet{colors.Reset}"

    # ADD ALL VARIABLES CHANGED TO DESCRIPTION
    desc = f"A Helmet made for the mountains, from the mountain creatures! You will be able to pounce like a wolf now." \
           f"\n{colors.Cyan}LVL REQUIRED: {colors.LightCyan}{lvl_req}{colors.Reset}" \
           f"\n{colors.Green}HP: {colors.LightGreen}{hp}" \
           f"\n{colors.White}Speed: {speed}" \
           f"\n{colors.Yellow}Armor: {colors.LightYellow}{armor}" \
           f"\n{colors.Magenta}CRC: {colors.LightMagenta}{crc}" \
           f"\n{colors.LightRed}Fire Res: {fire_resistance * 100}%" \
           f"\n{colors.LightYellow}Shock Res: {shock_resistance * 100}%{colors.Reset}" \
           f"\n{colors.LightGreen}Sell Price: {colors.Green}${sell}{colors.Reset}"

    def __init__(self):
        pass

    # used if item is craftable, do not delete
    @staticmethod
    def print_recipe():
        string = ""
        for key in mountain_helmet.recipe:
            string = f"{string}| {mountain_helmet.recipe[key]}x {key.name} | "

        return string

