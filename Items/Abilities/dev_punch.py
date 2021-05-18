from Utility.colors import colors
from Styles.brawler import brawler


class dev_punch:

    type = "ability"

    # import the style of the ability
    style = brawler

    discovered = False

    name = f"{colors.LightGreen}Devastating Punch{colors.Reset}"
    desc = f"An incredibly hard punch that is sure to hurt your opponents; but to you, too." \
           f"\n{colors.Magenta}Type:{colors.LightMagenta}{style.name}{colors.Reset}" \
           f"\n{colors.LightBlue}Special: {colors.LightCyan}If casted only once, deal an extra 10 damage.{colors.Reset}"

    # +1
    cooldown = 2
    cur_cd = 0

    # variables like damage and others that this ability might use
    dmg = 0
    self_dmg = 0

    def __init__(self):

        dmg = self.dmg
        cur_cd = self.cur_cd
        cooldown = self.cooldown

    def action(self, combat, caster, casted):

        base_dmg = (35 + (.15 * caster.dmg))
        damage = int(base_dmg * (1-casted.armor_percent)) - casted.armor

        if damage > 0:
            print(f"{colors.LightBlue}{caster.name}{colors.Reset} dealt {colors.Yellow}{damage}{colors.Reset} damage to {colors.LightRed}{casted.name}{colors.Reset}!\n")
            casted.hp -= damage
            print(f"{caster.name}{colors.LightRed} just hurt themselves for 15 damage!{colors.Reset}")
            caster.hp -= 15

        else:
            print(f"{colors.LightBlue}{caster.name}{colors.Red} could not get past {colors.LightRed}{casted.name}{colors.Reset}'s defense!\n")

    # if this move is only used once, deal an extra 10 damage.
    def special(self, combat, caster, casted):

        # see how many dev punches we did
        count = 0
        for ability in combat.swings:
            if ability == self.name:
                count += 1

        # checking if combat.swings == 0 is basically checking to see if your turn is over before applying.
        if count == 1 and combat.swing == 0 and self.cur_cd <= 0:
            self.cur_cd = self.cooldown
            print(f"\n{caster.name} has gotten {self.name}'s special, {colors.Magenta}and has dealt {colors.LightMagenta}10 {colors.Magenta}extra damage!{colors.Reset}")

            casted.hp -= 10
