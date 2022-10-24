from random import randint

from Items.Abilities.Resolute.body_bash import body_bash
from Utility.colors import colors

from Items.Materials.golagtatite import golagtatite


class baby_golagmite:
    type = "enemy"

    maxhp = 0
    hp = 0
    armor = 0
    armor_percent = 0.05  # this will never be random
    dmg = 0
    speed = 0
    crc = 0.0 # this will never be random
    fire_resistance = 1
    shock_resistance = 0.3
    poison_amp = 0.0

    combat_level = {"dueling": 0,
                    "eldric": 0,
                    "nimbilic": 0,
                    "resolute": 1,
                    "elitist": 0,
                    "standard": 0,
                    "brawler": 0}

    hp_range = (30, 35)
    armor_range = (6, 9)
    dmg_range = (8, 10)
    speed_range = (-2, -1)
    xp_drop_range = (10, 15)

    abilities = [body_bash]

    loot_table = {range(0, 51): golagtatite, range(49, 100): None}

    wclass = "brawling"

    name = "Baby Golagmite"
    undiscovered_desc = "In the distance, you see a small sized chunk of ore. This did not shock you, until the chunk of ore grew legs and started walking towards you. You have found a Baby Golagmite!"
    desc = "A golem-like creature that covers its back in ore, in order to hide itself from predators. Found in Stronia, these creatures are slow, but resilient." \
           "\nThis particular one is a baby. It belongs to a massive family local to only Stronia." \
           f"{colors.Green}HP Range: {colors.LightGreen}{hp_range[0]} - {hp_range[1]} {colors.Green}HP\n" \
           f"{colors.Yellow}Armor Range: {colors.LightYellow}{armor_range[0]} - {armor_range[1]} {colors.Yellow}Armor\n" \
           f"{colors.Red}Damage Range: {colors.LightRed}{dmg_range[0]} - {dmg_range[1]} {colors.Red}DMG\n" \
           f"{colors.Magenta}CRC: {colors.LightMagenta}{crc} {colors.Magenta}CRC\n" \
           f"{colors.Blue}SPD Range: {colors.LightBlue}{speed_range[0]} - {speed_range[1]} {colors.Blue}SPD{colors.Reset}\n" \
           f"{colors.Cyan}XP Range: {colors.LightCyan}{xp_drop_range[0]} - {xp_drop_range[1]} {colors.Cyan}XP{colors.Reset}" \
           f"{colors.White}Abilities: {abilities[0].name}\n" \
           f"{colors.Yellow}Weapon Class: {colors.LightYellow}{wclass.upper()}" \
           f"{colors.Magenta}Combat Levels: {colors.LightMagenta} Resolute: 1" \
           f"{colors.Yellow}Drops: {golagtatite.name} (50% Chance)\n"

    def __init__(self, maxhp, armor, dmg, crc, speed):
        self.maxhp = maxhp
        self.hp = self.maxhp
        self.armor = armor
        self.dmg = dmg
        self.crc = crc
        self.speed = speed

    @staticmethod
    def choose(combat):
        return combat.enemy_list[0]

    @staticmethod
    def drop():
        item = randint(0, 99)
        for dict_key in baby_golagmite.loot_table:
            if item in dict_key:
                return baby_golagmite.loot_table[dict_key]

    @staticmethod
    def money():
        return randint(10, 15)
