from random import random

from Effects.burn import burn
from Effects.poison import poison
from Styles.standard import standard
from Utility.colors import colors
from Utility.damage import damage
from Utility.dialogue import dialogue

class venom_strike:

    # ABILITIES CAN BE RACE LOCKED
    # THIS IS DONE THROUGH THE WAY IT IS DROPPED, NOT THROUGH THE ABILITY
    # YOU SHOULD NEVER HAVE AN ABILITY THAT IS UNUSABLE BY YOUR RACE

    # DO NOT CHANGE THIS; the lexicon uses this
    type = "ability"

    # import the style of the ability
    style = standard

    # cooldown should be +1 of the ability's actual cooldown; this is because of how combat cooldowns work
    cooldown = 3

    # ability name and description
    # if the description has a filled in variable, you do not need to change it
    name = f"{colors.White}Venom Strike{colors.Reset}"
    desc = f"Strike your opponent with your weapon, and if you crit, poison your opponent." \
           f"\n{colors.Magenta}Type: {colors.LightMagenta}{style.name}{colors.Reset}" \
           f"\n{colors.Blue}Special: {colors.LightBlue}If your opponent is also Burning, deal an extra 12 damage." \
           f"\n{colors.Green}Special Cooldown: {colors.LightGreen}{cooldown-1} Rounds" \
           f"\n{colors.Red}Damage: {colors.LightRed}8 + 30% of your damage" \
           f"\n{colors.Green}Effect: {colors.LightGreen}If you crit, poison your opponent for 10 damage for 3 turns" \
           f"\n{colors.Yellow}Level Bonus: {colors.LightYellow}For every Standard level, add 3 damage to your special{colors.Reset}"

    # DO NOT CHANGE THIS; combat uses this
    cur_cd = 0

    # Extra global variables this ability needs can be put here; you can put as many as you want

    # a constructor is not necessary
    def __init__(self):
        pass

    # when the ability is called in combat, this runs
    def action(self, combat, caster, casted):

        dmg = 8 + (.3 * caster.dmg)
        damage.deal(combat, caster, casted, dmg, False, 0, 0, self.style)

        if random() <= caster.crc:
            self.check_effect(combat, caster, casted)

    # when your ability is cast, combat then runs special. When all your swings are done, combat calls special again.
    # this means that you can use the last special call to view all abilities used (see devastating punch) or use it just once on the first call (see bull swipe)
    def special(self, combat, caster, casted):

        has_burn = False
        for effect in combat.effects[casted.type]:
            if effect.type == burn.type:
                has_burn = True

        if self.cur_cd <= 0 and has_burn:
            self.cur_cd = self.cooldown
            special_damage = 12

            for level in range(0, caster.combat_level["standard"]):
                special_damage += 3

            dialogue.dia(None, f"{caster.name} has casted {self.name}'s special, and attacks your burn marks for {special_damage} damage!")
            damage.deal(combat, caster, casted, special_damage, False, 0, 0, self.style)

    # use this method ONLY if this ability applies an effect
    # delete this method if your ability has no effect; this is an internal ability and does not interact with combat
    def check_effect(self, combat, caster, casted):

        effect_count = 0
        for effect in combat.effects[casted.type]:

            if effect.type == poison.type:
                effect_count += 1

        if effect_count < poison.stack:  # changes how many times this effect can stack
            combat.effects[casted.type].append(poison(combat, caster, casted, 12, 3))
