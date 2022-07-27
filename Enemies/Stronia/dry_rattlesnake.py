from random import randint

from Effects.poison import poison
from Items.Abilities.Standard.stab import stab
from Items.Abilities.Standard.venom_strike import venom_strike
from Items.Accessories.poisoned_rattle import poisoned_rattle
from Items.Materials.snake_fang import snake_fang
from Utility.colors import colors

class dry_rattlesnake:
    type = "enemy"

    maxhp = 0
    hp = 0
    armor = 0
    armor_percent = 0.0  # this will never be random
    dmg = 0
    speed = 0
    crc = 0.2  # this will never be random
    fire_resistance = 0.3  # this will never be random
    shock_resistance = 0.1  # this will never be random
    poison_amp = 0.12

    combat_level = {"dueling": 0,
                    "eldric": 0,
                    "nimbilic": 0,
                    "resolute": 0,
                    "elitist": 0,
                    "standard": 1,
                    "brawler": 0}

    hp_range = (35, 40)
    armor_range = (3, 6)
    dmg_range = (10, 15)
    speed_range = (2, 4)
    xp_drop_range = (10, 15)

    abilities = [venom_strike, stab]

    loot_table = {range(0, 90): snake_fang, range(89, 100): poisoned_rattle}  # 90% chance (0 - 89) and 10% chance (90 - 99)
    wclass = "brawling"

    name = "Dry Rattlesnake"
    undiscovered_desc = "There are scary stories of encountering the noise of a rattlesnake in the Barren Lands. Unfortunately for you, you have heard it today."
    desc = "Fast snakes that reside in Stronia and Cyliac, these Rattlesnakes will get the pounce on you and poison you.\n" \
           f"{colors.Green}HP Range: {colors.LightGreen}{hp_range[0]} - {hp_range[1]} {colors.Green}HP\n" \
           f"{colors.Yellow}Armor Range: {colors.LightYellow}{armor_range[0]} - {armor_range[1]} {colors.Yellow}Armor\n" \
           f"{colors.Red}Damage Range: {colors.LightRed}{dmg_range[0]} - {dmg_range[1]} {colors.Red}DMG\n" \
           f"{colors.Magenta}CRC: {colors.LightMagenta}{crc} {colors.Magenta}CRC\n" \
           f"{colors.Blue}SPD Range: {colors.LightBlue}{speed_range[0]} - {speed_range[1]} {colors.Blue}SPD{colors.Reset}\n" \
           f"{colors.Cyan}XP Range: {colors.LightCyan}{xp_drop_range[0]} - {xp_drop_range[1]} {colors.Cyan}XP{colors.Reset}" \
           f"{colors.White}Abilities: {abilities[0].name}, {abilities[1].name}\n" \
           f"{colors.Yellow}Drops: {snake_fang.name} (90% Chance), {poisoned_rattle.name} (10% Chance)\n"

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

        has_poison = False
        for effect in combat.effects["player"]:
            if effect.type == poison.type:
                has_poison = True

        if has_poison:
            return combat.enemy_list[1]

        return combat.enemy_list[randint(0, 1)]

    # drops items
    @staticmethod
    def drop():
        item = randint(0, 99)  # picks a random number to see if it falls in the range if one of the items in loot_table
        for dict_key in dry_rattlesnake.loot_table:
            if item in dict_key:
                return dry_rattlesnake.loot_table[dict_key]

    # drops money
    @staticmethod
    def money():
        return randint(5, 10)
