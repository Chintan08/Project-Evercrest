from Utility.colors import colors
from Enemies.Stronia.golagmite import golagmite
from random import randint, randrange

class barren_land:

    name = "The Barren Lands"
    desc = f"{colors.LightCyan}Stronia is filled with empty lands if you go looking for them. But these lands also pose a great danger...{colors.Reset}"
    undiscovered_desc = f"{colors.LightCyan}Everywhere you look; nothing. In a kingdom so dense, you can expect to find these kinds of places. Welcome to the Barren Lands.{colors.Reset}"
    type = "location"

    # fill this list in with more enemies, and range, which is the probability
    enemies = {range(0,2): golagmite}

    # bosses are found in the last tier of an area
    boss = []

    discovered = False

    # you need this tier to be able to visit
    min_tier = 0

    @staticmethod
    def pick_enemy():
        enemy = randint(0,1)

        for dict_key in barren_land.enemies:
            if enemy in dict_key:
                picked = barren_land.enemies[dict_key]
                return picked(randint(picked.hp_range[0], picked.hp_range[1]), randrange(picked.armor_range[0], picked.armor_range[1]), randint(picked.dmg_range[0], picked.dmg_range[1]), randint(picked.crc_range[0], picked.crc_range[1]), randint(picked.speed_range[0], picked.speed_range[1]))
