from Utility.colors import colors


class galed(object):

    name = f"{colors.LightYellow}Galed{colors.Reset}"
    descriptor = f"{name}" \
                 f"\nGaled people have heightened senses and brainpower, allowing them to accomplish things no ordinary man can do. Whether it is to be a great warrior or scientist, all is possible if you are a Galed." \
                 f"\nYou are able to learn incredibly quickly. You will gain increased Combat XP bonuses to aid in your combative journey." \
                 f"\nGaled are far more reactive on the field, and as such, gain speed bonuses, and critical chance bonuses. They are weak early on in their lives, but as they progress, they grow faster than anyone."\

    hp = 75.0
    dmg = 7.0
    armor = 0.0
    armor_percent = 0.0
    crc = 0.05
    speed = 1.0
    xp_bonus = 1.15 # keep this at +1 because this makes sure you do not multiply by something less than 1

    hp_scale = 3.0
    dmg_scale = 2.0
    armor_scale = 0.0
    armor_percent_scale = 0.0
    crc_scale = 0.05
    spd_scale = 0.25
    xp_scale = 0.025

    # if you are immune to Burns, you will not take any damage from periodic fire damage.
    fire_resistance = 0.0
    shock_resistance = 0.0
    fire_resistance_scale = 0.0
    shock_resistance_scale = 0.0
