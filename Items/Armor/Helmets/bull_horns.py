from Utility.colors import colors


class bull_horns:

    # every equipment piece has all the power to change any stat
    dmg = 15.0
    crc = 0.0
    hp = 30.0
    speed = 0.0
    armor = 5.0
    armor_percent = 0.0
    xp_bonus = 0.0
    fire_resistance = 0.05
    shock_resistance = 0.0
    poison_amp = 0.0

    type = "helmet"

    recipe = {}
    sell = 50
    buy = 0

    lvl_req = 3

    name = f"{colors.Blue}Bull Horns{colors.Reset}"
    desc = f"Taken from the Gray Bull himself, these horns imbue you with a confidence you never knew you had. And no, you can't ask how to wear these." \
           f"\n{colors.Cyan}LVL REQUIRED: {colors.LightCyan}{lvl_req}{colors.Reset}" \
           f"\n{colors.Green}HP: {colors.LightGreen}{hp}{colors.Reset}" \
           f"\n{colors.Red}DMG: {colors.LightRed}{dmg}{colors.Reset} " \
           f"\n{colors.Magenta}ARMOR: {colors.LightMagenta}{armor}{colors.Reset}" \
           f"\n{colors.LightGreen}Sell Price: {colors.Green}${sell}{colors.Reset}"

    def __init__(self):
        pass