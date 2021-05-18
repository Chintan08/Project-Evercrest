from colored import fore, style

class grayed:

    descriptor = fore.DARK_RED_1 + "Grayed " + style.RESET + \
                 "\nGrayed are powerful humans, and are known to be the masters of fire. While each Grayed are different amongst themselves, they all burn the same within." \
                 "\nTheir skin lets them be immune to " + fore.DARK_ORANGE_3B + "Burns" + style.RESET + ".\n"

    hp = 100.0
    dmg = 12.0
    armor = 0.0
    crc = 0.0
    speed = 0.0

    hp_scale = 5.0
    dmg_scale = 1.5
    armor_scale = 0.0
    armor_percent_scale = 0.0
    crc_scale = 0.0
    spd_scale = 0.0

    # if you are immune to Burns, you will not take any damage from periodic fire damage.
    immune_to_burn = True