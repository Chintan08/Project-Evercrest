from Utility.colors import colors
from Styles.standard import standard
from Utility.damage import damage
from Utility.dialogue import dialogue


class stab(object):

    type = "ability"
    style = standard

    # +1
    cooldown = 3

    name = f"{colors.White}Stab{colors.Reset}"
    desc = f"A simple, short stab at your opponent. This ability cannot crit." \
           f"\n{colors.Magenta}Type: {colors.LightMagenta}{style.name}{colors.Reset}" \
           f"\n{colors.Blue}Special: {colors.LightBlue}When {name} {colors.LightBlue}is used 3 times in your Swings, it will be used again." \
           f"\n{colors.Green}Special Cooldown: {colors.LightGreen}{cooldown-1} Rounds" \
           f"\n{colors.Red}Damage: {colors.LightRed}8 + 25% of your damage." \
           f"\n{colors.Yellow}Level Bonus: {colors.LightYellow}For every Standard level, deal an extra 3 flat damage.{colors.Reset}"

    cur_cd = 0

    dmg = 0

    def __init__(self):
        pass

    def action(self, combat, caster, casted):

        # Standard Level Bonus
        # TODO: look into this more when balancing
        bonus_damage = 0
        for index in range(0, caster.combat_level["standard"]):
            bonus_damage += 3

        base_dmg = 8 + (.25 * caster.dmg) + bonus_damage
        damage.deal(combat, caster, casted, base_dmg, False, 0, 0, self.style)

    def special(self, combat, caster, casted):

        count = 0
        for ability in combat.swings:
            if ability.name == self.name:
                count += 1

        # if stab is used 3 times, then special is procced
        if count == 3 and self.cur_cd <= 0:
            self.cur_cd = self.cooldown

            dialogue.dia(None, f"\n{caster.name} has gotten {self.name}'s special, and has casted it one more time.")
            combat.styles.append(self.style)
            combat.swings.append(self)
            # call action again to mimmick another attack
            self.action(combat, caster, casted)
