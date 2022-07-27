from random import random

from Utility.colors import colors


class damage:

    last_mitigated_damage_value = 0
    last_premitigated_damage_value = 0

    damage_values = {"dueling": 0, "eldric": 0, "nimbilic": 0, "resolute": 0, "elitist": 0, "standard": 0, "brawler": 0}

    @staticmethod
    # can_crit is a boolean, crit_amp is the percentage increase of damage
    # crit_amp is a value above 1.0
    # when using damage.deal, have the pre-mitigated damage set beforehand
    def deal(combat, caster, casted, dmg, can_crit, crit_amp, crit_chance, style):

        damage_color = colors.Yellow

        # reset it every time we deal damage
        damage.last_mitigated_damage_value = 0

        damage.last_premitigated_damage_value = dmg

        # crit check
        if can_crit:
            if random() <= crit_chance:
                dmg *= crit_amp
                damage_color = colors.LightCyan

        dmg = int((dmg * (1 - casted.armor_percent)) - casted.armor)
        damage.last_mitigated_damage_value = dmg

        if dmg > 0:
            print(f"{colors.LightBlue}{caster.name}{colors.Reset} dealt {damage_color}{dmg}{colors.Reset} damage to {colors.LightRed}{casted.name}{colors.Reset}!")
            casted.hp -= dmg

            # store damage dealt into proper dictionary value
            # because abilities pass style objects instead of strings, we send style.style as add_to_values just wants the string
            damage.add_to_values(caster, style.style, dmg)

        else:
            print(f"{colors.LightBlue}{caster.name}{colors.Red} could not get past {colors.LightRed}{casted.name}{colors.Reset}'s defense!\n")

    @staticmethod
    # returns the value of the last post-mitigated damage value
    # useful for abilities that need to know the value of their damage after considering defenses
    def get_mitigated_value():
        return damage.last_mitigated_damage_value

    # returns the value of the last pre-mitigated damage value
    @staticmethod
    def get_premitigated_value():
        return damage.last_premitigated_damage_value

    @staticmethod
    # iterates through dictionary, sees if ability style matches dict style, and then adds damage to that category. used for XP calculations in Combat/Player
    # this method can be used by any class, especially if they do not use damage.deal()
    # ability_style is the STRING, not the OBJECT
    def add_to_values(caster, ability_style, damage_dealt):

        if caster.type == "player":
            for style in damage.damage_values:
                if ability_style == style:
                    damage.damage_values[style] += damage_dealt

    @staticmethod
    # clears all damage values from the dict above, used in combat
    def clear_values():
        for style in damage.damage_values:
            damage.damage_values[style] = 0

    @staticmethod
    def get_values():
        return damage.damage_values
