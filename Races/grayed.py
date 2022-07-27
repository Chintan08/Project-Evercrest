from Utility.colors import colors


class grayed(object):

    name = f"{colors.Red}Grayed{colors.Reset}"
    descriptor = f"{name}" \
                 f"\nGrayed are powerful humans, and are known to be the masters of fire. While each Grayed are different amongst themselves, they all burn the same within." \
                 f"\nTheir skin lets them be immune to {colors.LightRed}Burns{colors.Reset}.\n"

    hp = 80.0
    dmg = 7.0
    armor = 0.0
    armor_percent = 0.0
    crc = 0.0
    speed = 0.0
    xp_bonus = 1.0 # keep this at 1 because this makes sure you do not multiply by something less than 1

    hp_scale = 3.0
    dmg_scale = 2.0
    armor_scale = 0.0
    armor_percent_scale = 0.0
    crc_scale = 0.0
    spd_scale = 0.0
    xp_scale = 0.0

    # if you are immune to Burns, you will not take any damage from periodic fire damage.
    fire_resistance = 1.0
    shock_resistance = 0.0

    fire_resistance_scale = 0.0
    shock_resistance_scale = 0.0
