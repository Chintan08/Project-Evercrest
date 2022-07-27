from random import random

from Utility.colors import colors

# an attack that has a chance to crit, using a ratio of your crit chance. Standard increases damage, Eldric increases % conversion.
from Utility.damage import damage
from Utility.dialogue import dialogue


class nimbilic:

    type = "style"
    style = "nimbilic"
    name = f"{colors.Yellow}Nimbilic{colors.Reset}"
    desc = f"A Nimbilic combo will cause another attack to occur, that can crit for 2x damage. The crit chance is a percentage of yours.\n" \
           f"\n{colors.Magenta}Enhancers{colors.Reset}:\n" \
           f"Eldric: Increases the conversion percentage of your critical chance.\n" \
           f"Standard: Increases the flat damage of the attack.\n" \
           f"{colors.Yellow}Level Bonus: Increase the critical strike amplifier by 10% per level{colors.LightYellow}\n"

    # TODO: nimbilic level bonus
    @staticmethod
    def action(combat, caster, casted):
        # these variables are the amount of times a style of an enhancer has occurred
        e_count = 0
        s_count = 0

        for style in combat.styles:

            if style.style == "standard":
                s_count += 1

            if style.style == "eldric":
                e_count += 1

        bonus_damage = 0
        for level in range(0, caster.combat_level["nimbilic"]):
            bonus_damage += .1

        # for each standard ability, increase the percentage of damage taken from your damage
        base_dmg = 10 + (caster.dmg * ((s_count * .10) + .10))

        # for each eldric ability, increase the % you take from the crc by 35%
        crit_chance = caster.crc * (.35 + (e_count * .35))

        dialogue.dia(None, f"\n{colors.LightMagenta}{caster.name} has performed a {nimbilic.name} {colors.LightMagenta}Combo!{colors.Reset}")

        damage.deal(combat, caster, casted, base_dmg, True, 3.0 + bonus_damage, crit_chance, nimbilic)

