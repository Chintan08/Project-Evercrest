from random import randint

from Items.Abilities.Resolute.body_bash import body_bash
from Items.Abilities.Elitist.bull_swipe import bull_swipe
from Items.Abilities.Standard.ignition import ignition
from Items.Armor.Helmets.bull_horns import bull_horns
from Utility.colors import colors


class gray_bull:
    type = "enemy"

    maxhp = 0
    hp = 0
    armor = 0
    armor_percent = 0.15  # this will never be random
    dmg = 0
    speed = 0
    crc = 0.1
    fire_resistance = 1  # this will never be random
    shock_resistance = 0.0  # this will never be random
    poison_amp = 0.0

    combat_level = {"dueling": 0,
                    "eldric": 0,
                    "nimbilic": 0,
                    "resolute": 2,
                    "elitist": 3,
                    "standard": 0,
                    "brawler": 3}

    xp_drop_range = (50, 62)
    hp_range = (140, 145)
    armor_range = (22, 32)
    dmg_range = (30, 40)
    speed_range = (1, 3)

    abilities = [bull_swipe, ignition, body_bash]

    loot_table = {range(0, 100): bull_horns}
    wclass = "brawling"

    name = "Grayed Bull"
    undiscovered_desc = "As you walk closer to Fort Anvil, you feel the ground shake underneath you. You feel a lot warmer than usual, almost as if you feel fire. When you look behind yourself, you unfortunately meet the eyes of a Gray Bull."
    desc = "A bull that had mutated and became a Grayed. The Gray Bull is incredibly devastating if not controlled properly.\n" \
           f"{colors.Green}HP Range: {colors.LightGreen}{hp_range[0]} - {hp_range[1]} {colors.Green}HP\n" \
           f"{colors.Yellow}Armor Range: {colors.LightYellow}{armor_range[0]} - {armor_range[1]} {colors.Yellow}Armor\n" \
           f"{colors.Red}Damage Range: {colors.LightRed}{dmg_range[0]} - {dmg_range[1]} {colors.Red}DMG\n" \
           f"{colors.Magenta}CRC: {colors.LightMagenta}{crc} {colors.Magenta}CRC\n" \
           f"{colors.Blue}SPD Range: {colors.LightBlue}{speed_range[0]} - {speed_range[1]} {colors.Blue}SPD{colors.Reset}\n" \
           f"{colors.Cyan}XP Range: {colors.LightCyan}{xp_drop_range[0]} - {xp_drop_range[1]} {colors.Cyan}XP{colors.Reset}" \
           f"{colors.White}Abilities: {abilities[0].name}, {abilities[1].name}\n" \
           f"{colors.Yellow}Drops: {bull_horns.name}\n"

    def __init__(self, maxhp, armor, dmg, crc, speed):
        self.maxhp = maxhp
        self.hp = self.maxhp
        self.armor = armor
        self.dmg = dmg
        self.crc = crc
        self.speed = speed

    @staticmethod
    def choose(combat):

        # if swing is 1, body bash
        if combat.swing == 1:
            return combat.enemy_list[2]

        return combat.enemy_list[randint(0, 1)]

    @staticmethod
    def drop():
        item = randint(0, 99)
        for dict_key in gray_bull.loot_table:
            if item in dict_key:
                return gray_bull.loot_table[dict_key]

    @staticmethod
    def money():
        return randint(80, 120)
