from colored import fore, style

from Utility.colors import colors


class human(object):

    name = f"{colors.White}Gene-Tampered{colors.Reset}"
    descriptor = f"{name}" \
                 "\nGene-Tampered are all that is left after Mt. Krion blew up. Their genetics were modified, but no changes were made." \
                 "\nWhile they are not exactly unique, they make it up for their lack of weaknesses other races receive.\n"

    hp = 85.0
    dmg = 8.0
    armor = 0.0
    armor_percent = 0.0
    crc = 0.0
    speed = 0.0
    xp_bonus = 1.0  # keep this at 1 because this makes sure you do not multiply by something less than 1

    hp_scale = 6.0
    dmg_scale = 2.0
    armor_scale = 0.0
    armor_percent_scale = 0.0
    crc_scale = 0.0
    spd_scale = 0.0
    xp_scale = 0.0

    fire_resistance = 0.0
    shock_resistance = 0.0
    fire_resistance_scale = 0.0
    shock_resistance_scale = 0.0
