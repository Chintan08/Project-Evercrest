from Utility.colors import colors
from Styles.standard import standard


class stab:

    type = "ability"
    style = standard

    discovered = False

    name = f"{colors.White}Stab{colors.Reset}"
    desc = f"A simple, short stab at your opponent. This ability cannot crit." \
           f"\n{colors.Magenta}Type:{colors.LightMagenta} Standard{colors.Reset}"

    # +1
    cooldown = 3
    cur_cd = 0

    dmg = 0

    def __init__(self):
        pass

    # TODO: for all enemies and abilities, implement percentage armor
    def action(self, combat, caster, casted):

        base_dmg = int(10 + (.45 * caster.dmg))
        dmg = (base_dmg * (1-casted.armor_percent)) - casted.armor

        if dmg > 0:
            print(f"{colors.LightBlue}{caster.name}{colors.Reset} dealt {colors.Yellow}{dmg}{colors.Reset} damage to {colors.LightRed}{casted.name}{colors.Reset}!\n")
            casted.hp -= dmg

        else:
            print(f"{colors.LightBlue}{caster.name}{colors.Red} could not get past {colors.LightRed}{casted.name}{colors.Reset}'s defense!\n")

    def special(self, combat, caster, casted):

        count = 0
        for ability in combat.swings:
            if ability == self.name:
                count+=1

        if count == 3 and self.cur_cd <= 0:
            self.cur_cd = self.cooldown

            print(f"\n{caster.name} has gotten {self.name}'s special, and has casted it once more time.")
            combat.styles.append(self.style)
            combat.swings.append(self.name)
            self.action(combat, caster, casted)