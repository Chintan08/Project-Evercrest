from Effects.burn import burn
from Effects.ignite import ignite
from Styles.standard import standard
from Utility.colors import colors
from Utility.dialogue import dialogue

class ignition:

    # ABILITIES CAN BE RACE LOCKED
    # THIS IS DONE THROUGH THE WAY IT IS DROPPED, NOT THROUGH THE ABILITY
    # YOU SHOULD NEVER HAVE AN ABILITY THAT IS UNUSABLE BY YOUR RACE

    # DO NOT CHANGE THIS; the lexicon uses this
    type = "ability"

    # import the style of the ability
    style = standard

    # cooldown should be +1 of the ability's actual cooldown; this is because of how combat cooldowns work
    cooldown = 6

    # ability name and description
    # if the description has a filled in variable, you do not need to change it
    name = f"{colors.White}Ignition{colors.Reset}"
    desc = f"A gray-only ability that makes you become Ignited. Every time you use it while Ignited, burn your opponent for 15 damage for 3 turns." \
           f"\n{colors.Magenta}Type: {colors.LightMagenta}{style.name}{colors.Reset}" \
           f"\n{colors.Blue}Special: {colors.LightBlue}If your opponent is Ignited, your Damage bonus increases by 5." \
           f"\n{colors.Green}Special Cooldown: {colors.LightGreen}{cooldown-1} Rounds" \
           f"\n{colors.Green}Effect: {colors.LightGreen}Ignition gives you 10 bonus damage for 3 turns. " \
           f"\n{colors.Yellow}Level Bonus: {colors.LightYellow}Increase Ignition bonus damage by 2 for each Standard level, including the Special.{colors.Reset}"

    # DO NOT CHANGE THIS; combat uses this
    cur_cd = 0

    # Extra global variables this ability needs can be put here; you can put as many as you want
    dmg = 0

    # a constructor is not necessary
    def __init__(self):
        pass

    # when the ability is called in combat, this runs
    def action(self, combat, caster, casted):

        if ignite.type in combat.get_effect_list(caster):

            effect_count = 0
            for effect in combat.effects[casted.type]:

                if effect.type == burn.type:
                    effect_count += 1

            if effect_count < burn.stack:
                combat.effects[casted.type].append(burn(combat, caster, casted, 15, 3))

    # when your ability is cast, combat then runs special. When all your swings are done, combat calls special again.
    # this means that you can use the last special call to view all abilities used (see devastating punch) or use it just once on the first call (see bull swipe)
    def special(self, combat, caster, casted):

        self.dmg = 10

        if self.cur_cd <= 0 and ignite.type in combat.get_effect_list(casted):
            self.cur_cd = self.cooldown

            dialogue.dia(None, f"{caster.name} sees you are {colors.LightRed}Ignited{colors.Reset}, and powers up!")
            self.dmg += 5

        for level in range(0, caster.combat_level["standard"]):
            self.dmg += 2

        self.check_effect(combat, caster, caster)

    # use this method ONLY if this ability applies an effect
    # delete this method if your ability has no effect; this is an internal ability and does not interact with combat
    def check_effect(self, combat, caster, casted):

        effect_count = 0
        for effect in combat.effects[casted.type]:

            if effect.type == ignite.type:
                effect_count += 1

        if effect_count < ignite.stack: # changes how many times this effect can stack
            combat.effects[casted.type].append(ignite(combat, caster, casted, self.dmg, 3))
