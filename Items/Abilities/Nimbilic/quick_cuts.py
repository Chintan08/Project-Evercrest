from random import random

from Effects.bleed import bleed
from Styles.nimbilic import nimbilic
from Utility.colors import colors
from Utility.damage import damage
from Utility.dialogue import dialogue

class quick_cuts:

    # ABILITIES CAN BE RACE LOCKED
    # THIS IS DONE THROUGH THE WAY IT IS DROPPED, NOT THROUGH THE ABILITY
    # YOU SHOULD NEVER HAVE AN ABILITY THAT IS UNUSABLE BY YOUR RACE

    # DO NOT CHANGE THIS; the lexicon uses this
    type = "ability"

    # import the style of the ability
    style = nimbilic

    # cooldown should be +1 of the ability's actual cooldown; this is because of how combat cooldowns work
    cooldown = 5

    # ability name and description
    # if the description has a filled in variable, you do not need to change it
    name = f"{colors.Yellow}Quick Cuts{colors.Reset}"
    desc = f"Slash your opponent deep for low damage, but get a 25% chance of causing them to bleed." \
           f"\n{colors.Magenta}Type: {colors.LightMagenta}{style.name}{colors.Reset}" \
           f"\n{colors.Blue}Special: {colors.LightBlue}If used 3 times, cut again for a fourth time. This cut can crit for 3x the damage, and if the ability crits, you will apply a bleed that deals damage equal to 6x your speed for 2 rounds.\n" \
           f"The critical strike chance for this ability is 75% of your Crit Chance." \
           f"\n{colors.Green}Special Cooldown: {colors.LightGreen}{cooldown-1} Rounds" \
           f"\n{colors.Red}Damage: {colors.LightRed}5 + 20% of your damage" \
           f"\n{colors.Green}Effect: {colors.LightGreen}Makes your opponent bleed for 10 damage for 3 rounds." \
           f"\n{colors.Yellow}Level Bonus: {colors.LightYellow}Increases the damage of the basic bleed by 3 and the chance of it occurring by 2.5% per level.{colors.Reset}"

    # DO NOT CHANGE THIS; combat uses this
    cur_cd = 0

    # Extra global variables this ability needs can be put here; you can put as many as you want
    bleed_damage = 10
    effect_duration = 0
    dmg = 0

    # a constructor is not necessary
    def __init__(self):
        pass

    # when the ability is called in combat, this runs
    def action(self, combat, caster, casted):

        self.dmg = 5 + (.2 * caster.dmg)

        bleed_chance = .25

        damage.deal(combat, caster, casted, self.dmg, True, 2, caster.crc, self.style)

        self.bleed_damage = 10
        if random() <= bleed_chance:
            for level in range(0, caster.combat_level["nimbilic"]):
                self.bleed_damage += 3

            self.effect_duration = 3
            self.check_effect(combat, caster, casted)

    # when your ability is cast, combat then runs special. When all your swings are done, combat calls special again.
    # this means that you can use the last special call to view all abilities used (see devastating punch) or use it just once on the first call (see bull swipe)
    def special(self, combat, caster, casted):

        count = 0
        for ability in combat.swings:
            if ability.name == self.name:
                count += 1

        # if stab is used 3 times, then special is procced
        if count == 3 and self.cur_cd <= 0:

            self.cur_cd = self.cooldown

            dialogue.dia(None, f"\n{caster.name} has gotten {self.name}'s special, and has cut one more time!")

            combat.styles.append(self.style)
            combat.swings.append(self)

            crit_chance = .75 * caster.crc

            damage.deal(combat, caster, casted, self.dmg, True, 3, crit_chance, self.style)

            # do effect checking again here because we are applying a new type of effect
            if random() <= crit_chance:

                self.bleed_damage = 6 * caster.speed
                if caster.speed <= 0:
                    self.bleed_damage = 1

                self.effect_duration = 2
                self.check_effect(combat, caster, casted)

    # use this method ONLY if this ability applies an effect
    # delete this method if your ability has no effect; this is an internal ability and does not interact with combat
    def check_effect(self, combat, caster, casted):

        effect_count = 0
        for effect in combat.effects[casted.type]:

            if effect.type == bleed.type:
                effect_count += 1

        if effect_count < bleed.stack: # changes how many times this effect can stack
            combat.effects[casted.type].append(bleed(combat, caster, casted, self.bleed_damage, self.effect_duration))
