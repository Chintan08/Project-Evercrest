from random import randint

from Items.Abilities.Brawling.dev_strike import dev_strike
from Items.Abilities.Standard.stab import stab
from Utility.colors import colors

class rockington_bandit:

    type = "enemy"

    maxhp = 0
    hp = 0
    armor = 0
    armor_percent = 0.0  # this will never be random
    dmg = 0
    speed = 0
    crc = 0.02 # this will never be random
    fire_resistance = 0.0 # this will never be random
    shock_resistance = 0.0 # this will never be random
    poison_amp = 0.0 # this will never be random

    combat_level = {"dueling": 0,
                    "eldric": 0,
                    "nimbilic": 0,
                    "resolute": 0,
                    "elitist": 0,
                    "standard": 0,
                    "brawler": 2}

    hp_range = (35, 35)
    armor_range = (5, 5)
    dmg_range = (10, 10)
    speed_range = (3, 3)
    xp_drop_range = (20, 20)

    abilities = [stab, dev_strike]

    # range is min, max-1
    loot_table = {range(0, 100): None}

    # what weapon class is this enemy
    wclass = "brawling"

    name = "Rockington Bandit"
    undiscovered_desc = "The Bandit cracks his knuckles, as he believes he has gotten you today."
    desc = "A bandit sent to ambush you in the Rockington Inn.\n" \
           f"{colors.Green}HP Range: {colors.LightGreen}{hp_range[0]} - {hp_range[1]} {colors.Green}HP\n" \
           f"{colors.Yellow}Armor Range: {colors.LightYellow}{armor_range[0]} - {armor_range[1]} {colors.Yellow}Armor\n" \
           f"{colors.Red}Damage Range: {colors.LightRed}{dmg_range[0]} - {dmg_range[1]} {colors.Red}DMG\n" \
           f"{colors.Magenta}CRC: {colors.LightMagenta}{crc} {colors.Magenta}CRC\n" \
           f"{colors.Blue}SPD Range: {colors.LightBlue}{speed_range[0]} - {speed_range[1]} {colors.Blue}SPD{colors.Reset}\n" \
           f"{colors.Cyan}XP Range: {colors.LightCyan}{xp_drop_range[0]} - {xp_drop_range[1]} {colors.Cyan}XP{colors.Reset}" \
           f"{colors.White}Abilities: {abilities[0].name, abilities[1].name}\n" \


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

        count = 0
        for ability in combat.swings:
            if ability.name == combat.enemy_list[1].name:
                count += 1

        if count == 0:
            return combat.enemy_list[1]

        else:
            return combat.enemy_list[0]

    # drops items
    @staticmethod
    def drop():
        item = randint(0, 99) # picks a random number to see if it falls in the range if one of the items in loot_table
        for dict_key in rockington_bandit.loot_table:
            if item in dict_key:
                return rockington_bandit.loot_table[dict_key]

    # drops money
    @staticmethod
    def money():
        return 25
