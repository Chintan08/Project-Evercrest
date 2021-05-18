from colored import fore, style

class human:

    descriptor = "yesn't"

    descriptor = fore.DARK_SEA_GREEN_1 + "Gene-Hammered" + style.RESET + \
                 "\nGene-Hammered are all that is left after Mt. Krion blew up. Their genetics were modified, but no changes were made." \
                 "\nWhile they are not exactly unique, they make it up for their lack of weaknesses other races receive.\n"

    hp = 120.0
    dmg = 15.0
    armor = 0.0
    crc = 0.0
    speed = 0.0

    hp_scale = 6.0
    dmg_scale = 3.0
    armor_scale = 0.0
    armor_percent_scale = 0.0
    crc_scale = 0.0
    spd_scale = 0.0

    # if you are immune to Burns, you will not take any damage from periodic fire damage.
    immune_to_burn = True