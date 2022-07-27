from random import randint

from Items.Abilities.Nimbilic.quick_cuts import quick_cuts
from Items.Abilities.Standard.stab import stab
from Items.Materials.wolf_pelt import wolf_pelt
from Utility.colors import colors


class mountain_wolf:
    type = "enemy"

    maxhp = 0
    hp = 0
    armor = 0
    armor_percent = 0.0  # this will never be random
    dmg = 0
    speed = 0
    crc = 0.05
    fire_resistance = 0.1  # this will never be random
    shock_resistance = 0.0  # this will never be random
    poison_amp = 0.0

    combat_level = {"dueling": 0,
                    "eldric": 0,
                    "nimbilic": 1,
                    "resolute": 0,
                    "elitist": 0,
                    "standard": 1,
                    "brawler": 0}

    hp_range = (45, 50)
    armor_range = (3, 6)
    dmg_range = (12, 14)
    speed_range = (1, 3)
    xp_drop_range = (10, 15)

    abilities = [stab, quick_cuts]

    loot_table = {range(0, 100): wolf_pelt}
    wclass = "brawling"

    name = "Mountain Wolf"
    undiscovered_desc = "As you walk across the Barren Lands, you hear an aggressive growl. Suddenly, a Mountain Wolf appears in front of you!"
    desc = "Wolves native to the Stronia Barren Lands, these creatures are incredibly efficient at killing things that don't have iron skin, including you.\n" \
           f"{colors.Green}HP Range: {colors.LightGreen}{hp_range[0]} - {hp_range[1]} {colors.Green}HP\n" \
           f"{colors.Yellow}Armor Range: {colors.LightYellow}{armor_range[0]} - {armor_range[1]} {colors.Yellow}Armor\n" \
           f"{colors.Red}Damage Range: {colors.LightRed}{dmg_range[0]} - {dmg_range[1]} {colors.Red}DMG\n" \
           f"{colors.Magenta}CRC: {colors.LightMagenta}{crc} {colors.Magenta}CRC\n" \
           f"{colors.Blue}SPD Range: {colors.LightBlue}{speed_range[0]} - {speed_range[1]} {colors.Blue}SPD{colors.Reset}\n" \
           f"{colors.Cyan}XP Range: {colors.LightCyan}{xp_drop_range[0]} - {xp_drop_range[1]} {colors.Cyan}XP{colors.Reset}" \
           f"{colors.White}Abilities: {abilities[0].name}, {abilities[1].name}\n" \
           f"{colors.Yellow}Drops: {wolf_pelt.name}\n"

    def __init__(self, maxhp, armor, dmg, crc, speed):
        self.maxhp = maxhp
        self.hp = maxhp
        self.armor = armor
        self.dmg = dmg
        self.crc = crc
        self.speed = speed

    # a method that chooses your next ability, using the context given through combat
    # specifically use combat.enemy_list, NOT the internal ability list
    @staticmethod
    def choose(combat):
        return combat.enemy_list[randint(0, 1)]

    # drops items
    @staticmethod
    def drop():
        item = randint(0, 99)  # picks a random number to see if it falls in the range if one of the items in loot_table
        for dict_key in mountain_wolf.loot_table:
            if item in dict_key:
                return mountain_wolf.loot_table[dict_key]

    # drops money
    @staticmethod
    def money():
        return randint(5, 10)
