from Styles.resolute import resolute
from Utility.colors import colors
from Utility.damage import damage
from Utility.dialogue import dialogue

class body_bash:

    # ABILITIES CAN BE RACE LOCKED
    # THIS IS DONE THROUGH THE WAY IT IS DROPPED, NOT THROUGH THE ABILITY
    # YOU SHOULD NEVER HAVE AN ABILITY THAT IS UNUSABLE BY YOUR RACE

    # DO NOT CHANGE THIS; the lexicon uses this
    type = "ability"

    # import the style of the ability
    style = resolute

    # cooldown should be +1 of the ability's actual cooldown; this is because of how combat cooldowns work
    cooldown = 3

    # ability name and description
    # if the description has a filled in variable, you do not need to change it
    name = f"{colors.Green}Body Bash{colors.Reset}"
    desc = f"Bash your opponent with your entire weight! The bigger you are, the more you'll do." \
           f"\n{colors.Magenta}Type: {colors.LightMagenta}{style.name}{colors.Reset}" \
           f"\n{colors.Blue}Special: {colors.LightBlue}If your opponent has less armor than you, deal extra damage equal to 50% of the armor difference + 15% of your maxHP." \
           f"\n{colors.Green}Special Cooldown: {colors.LightGreen}{cooldown-1} Rounds" \
           f"\n{colors.Red}Damage: {colors.LightRed}15% of your damage + 25% of your maxHP" \
           f"\n{colors.Yellow}Level Bonus: {colors.LightYellow}Increase the amount of % maxHP in your Special by 2.5% for each Resolute level{colors.Reset}"

    # DO NOT CHANGE THIS; combat uses this
    cur_cd = 0

    # Extra global variables this ability needs can be put here; you can put as many as you want

    # a constructor is not necessary
    def __init__(self):
        pass

    # when the ability is called in combat, this runs
    def action(self, combat, caster, casted):

        dmg = (.15 * caster.dmg) + (.25 * caster.maxhp)
        damage.deal(combat, caster, casted, dmg, False, 0, 0, self.style)
        combat.swing = 0

    # when your ability is cast, combat then runs special. When all your swings are done, combat calls special again.
    # this means that you can use the last special call to view all abilities used (see devastating punch) or use it just once on the first call (see bull swipe)
    def special(self, combat, caster, casted):

        if self.cur_cd <= 0 and casted.armor < caster.armor and self in combat.swings:

            self.cur_cd = self.cooldown

            dialogue.dia(None, f"{caster.name} has gotten {self.name}'s special, and is taking advantage of your low armor!")

            bonus_damage = 0
            for level in range(0, caster.combat_level["resolute"]):
                bonus_damage += .025

            damage.deal(combat, caster, casted, ((caster.armor - casted.armor) * .5 + ((.15 + bonus_damage) * caster.maxhp)), False, 0, 0, self.style)

