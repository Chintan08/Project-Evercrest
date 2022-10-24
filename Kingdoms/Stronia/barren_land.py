from Enemies.Stronia.Bosses.gray_bull import gray_bull
from Enemies.Stronia.dry_rattlesnake import dry_rattlesnake
from Enemies.Stronia.mountain_wolf import mountain_wolf
from Utility.colors import colors
from Enemies.Stronia.baby_golagmite import baby_golagmite
from random import randint, randrange

class barren_land:

    name = "The Barren Lands"
    desc = f"{colors.LightCyan}Stronia is filled with empty lands if you go looking for them. But these lands also pose a great danger...{colors.Reset}"
    undiscovered_desc = f"{colors.LightCyan}As you venture out the kingdom and into the valley, you are surprised to see nothing around you. Welcome to the Barren Lands.{colors.Reset}"
    type = "location"

    # fill this list in with more enemies, and range, which is the probability
    enemies = {range(0, 1): baby_golagmite, range(1, 2): mountain_wolf, range(2, 3): dry_rattlesnake}

    # bosses are found in the last tier of an area
    boss = [gray_bull]

    # you need this tier to be able to visit
    min_tier = 0

    @staticmethod
    def pick_enemy():

        enemy = randint(0, 2)  # range is not inclusive, so we make sure we do n-1

        for dict_key in barren_land.enemies:
            if enemy in dict_key:
                picked = barren_land.enemies[dict_key]
                return picked(randint(picked.hp_range[0], picked.hp_range[1]), randrange(picked.armor_range[0], picked.armor_range[1]), randint(picked.dmg_range[0], picked.dmg_range[1]), picked.crc, randint(picked.speed_range[0], picked.speed_range[1]))

    @staticmethod
    def pick_boss():
        picked = barren_land.boss[0]
        return picked(randint(picked.hp_range[0], picked.hp_range[1]), randrange(picked.armor_range[0], picked.armor_range[1]), randint(picked.dmg_range[0], picked.dmg_range[1]), picked.crc, randint(picked.speed_range[0], picked.speed_range[1]))
