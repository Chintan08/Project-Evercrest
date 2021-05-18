from random import randint
from Utility.colors import colors

from Items.Abilities.stab import stab
from Items.Materials.golagtatite import golagtatite


class golagmite:
    type = "enemy"

    maxhp = 0
    hp = 0
    armor = 0
    armor_percent = 0.0  # this will never be random
    dmg = 0
    speed = 0
    crc = 0.0

    hp_range = (70, 90)
    armor_range = (5, 20)
    dmg_range = (10, 15)
    speed_range = (-1, 2)
    crc_range = (0, 0)

    can_be_burned = True

    abilities = [stab]

    discovered = False

    loot_table = {range(0, 4): golagtatite}

    name = "Golagmite"
    undiscovered_desc = "A large chunk of ore is walking towards you, with its every footstep sending a shock to your " \
                        "heart. You have found the middle child of the Golum family. "
    desc = "A large chunk of ore, found in Stronia.\n" \
           f"{colors.Green}HP Range{colors.Reset}: {colors.LightGreen}{hp_range[0]} - {hp_range[1]} {colors.Green}HP\n" \
           f"{colors.Yellow}Armor Range: {colors.LightYellow}{armor_range[0]} - {armor_range[1]} {colors.Yellow}Armor\n" \
           f"{colors.Red}Damage Range: {colors.LightRed}{dmg_range[0]} - {dmg_range[1]} {colors.Red}DMG\n" \
           f"{colors.Magenta}CRC Range: {colors.LightMagenta}{crc_range[0]} - {crc_range[1]} {colors.Magenta}CRC\n" \
           f"{colors.Blue}SPD Range: {colors.LightBlue}{speed_range[0]} - {speed_range[1]} {colors.Blue}SPD{colors.Reset}\n" \
           f"{colors.White}Abilities: {abilities[0].name}\n"

    def __init__(self, maxhp, armor, dmg, crc, speed):
        self.maxhp = maxhp + 1000
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
        item = randint(0, 3)
        for dict_key in golagmite.loot_table:
            if item in dict_key:
                return golagmite.loot_table[dict_key]

    @staticmethod
    def money():
        return randint(30, 60)
