from Utility.colors import colors


class rustic_helmet:

    # every equipment piece has all the power to change any stat
    # think of items as stat sticks, change the stats here
    dmg = 0
    crc = 0.0
    hp = 5.0
    speed = 0.0
    armor = 2.0

    # keep as decimals
    armor_percent = 0.0
    xp_bonus = 0.0
    fire_resistance = 0.01
    shock_resistance = 0.0
    poison_amp = 0.0

    # is this a helmet, chestplate, leggings, or boots
    type = "helmet"

    # if this item is craftable, what do you need to craft it? craftable items must be added to crafting.py
    # recipe is a dictionary, use this format:
    # MATERIAL: AMOUNT
    recipe = {}

    # SET TO NONE IF YOU DO NOT WANT IT TO BE SELLABLE
    sell = 35

    # set buying price, must add item to respective kingdom's shop market
    buy = 70

    # what level do you need to be to equip this item?
    lvl_req = 0

    name = f"{colors.White}Rustic Helmet{colors.Reset}"

    # ADD ALL VARIABLES CHANGED TO DESCRIPTION
    desc = f"This helmet has had better days, but it still protects you, technically..." \
           f"\n{colors.Cyan}LVL REQUIRED: {colors.LightCyan}{lvl_req}{colors.Reset}" \
           f"\n{colors.Green}HP: {colors.LightGreen}{hp}" \
           f"\n{colors.Yellow}Armor: {colors.LightYellow}{armor}" \
           f"\n{colors.LightRed}Fire Resist: {fire_resistance * 100}%{colors.Reset}" \
           f"\n{colors.LightGreen}Sell Price: {colors.Green}${sell}{colors.Reset}"

    def __init__(self):
        pass

    # used if item is craftable, do not delete
    @staticmethod
    def print_recipe():
        string = ""
        for key in rustic_helmet.recipe:
            string = f"{string}| {rustic_helmet.recipe[key]}x {key.name} | "

        return string

