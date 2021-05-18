from Utility.colors import colors
from Enemies.Stronia.golagmite import golagmite
from random import randint

class fort_anvil:

    name = "Fort Anvil"
    desc = f"{colors.LightCyan}One of the great forts that kept the kingdom safe for a very long time.{colors.Reset}"
    undiscovered_desc = f"{colors.LightCyan}The fort of stories is in front of your eyes; but instead of knights, there are villains.{colors.Reset}"
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

        for dict_key in fort_anvil.enemies:
            if enemy in dict_key:
                return fort_anvil.enemies[dict_key]