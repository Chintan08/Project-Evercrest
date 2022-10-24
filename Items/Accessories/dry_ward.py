from Utility.colors import colors


class dry_ward:

    # every equipment piece has all the power to change any stat
    dmg = 0
    crc = 0
    hp = 0.0
    speed = 1.0
    armor = 0.0
    armor_percent = 0.0
    xp_bonus = 0.0
    fire_resistance = 0.06
    shock_resistance = 0.02
    poison_amp = 0

    type = "accessory"

    recipe = {}
    sell = 35
    buy = 70

    lvl_req = 0

    name = f"{colors.White}Dry Ward{colors.Reset}"
    desc = f"A crudely crafted piece of iron. It's said that this will ward you from the dangers of dry creatures." \
           f"\n{colors.White}Speed: {speed}" \
           f"\n{colors.LightRed}Fire Res: {fire_resistance * 100}%" \
           f"\n{colors.LightYellow}Shock Res: {shock_resistance * 100}%" \
           f"\n{colors.LightGreen}Sell Price: {colors.Green}${sell}{colors.Reset}"

    def __init__(self):
        pass
