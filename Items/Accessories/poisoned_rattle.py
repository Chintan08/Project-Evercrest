from Utility.colors import colors


class poisoned_rattle:

    # every equipment piece has all the power to change any stat
    dmg = 2.0
    crc = 0.02
    hp = 0.0
    speed = 0.0
    armor = 0.0
    armor_percent = 0.0
    xp_bonus = 0.0
    fire_resistance = 0.0
    shock_resistance = 0.0
    poison_amp = 0.05

    type = "accessory"

    recipe = {}
    sell = 20
    buy = 0

    lvl_req = 0

    name = f"{colors.LightGreen}Poisoned Rattle{colors.Reset}"
    desc = f"This rattle dropped from a Rattlesnake still is poisoned. It looks like it enhances your poison effects!" \
           f"\n{colors.Red}Damage: {colors.LightRed}{dmg}" \
           f"\n{colors.Magenta}CRC%: {colors.LightMagenta}{crc}" \
           f"\n{colors.LightGreen}Poison Amp: {poison_amp * 100}%" \
           f"\n{colors.LightGreen}Sell Price: {colors.Green}${sell}{colors.Reset}"

    def __init__(self):
        pass