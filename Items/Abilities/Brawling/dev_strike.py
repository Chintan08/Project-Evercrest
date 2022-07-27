from Utility.colors import colors
from Styles.brawler import brawler
from Utility.damage import damage
from Utility.dialogue import dialogue


class dev_strike:

    type = "ability"

    # import the style of the ability
    style = brawler

    # +1
    cooldown = 2

    name = f"{colors.LightGreen}Devastating Strike{colors.Reset}"
    desc = f"An incredibly hard strike that is sure to hurt your opponents; but you will face repercussions, too. This ability can not crit." \
           f"\n{colors.Magenta}Type: {colors.LightMagenta}{style.name}{colors.Reset}" \
           f"\n{colors.Blue}Special: {colors.LightBlue}If casted only once, and your weapon class is Brawling, deal an extra 10 damage.{colors.Reset}" \
           f"\n{colors.Green}Special Cooldown: {colors.LightGreen}{cooldown-1} Rounds" \
           f"\n{colors.Red}Damage: {colors.LightRed}35 + 15% of your damage. You take 10% of mitigated damage dealt." \
           f"\n{colors.Yellow}Level Bonus: {colors.LightYellow}"

    cur_cd = 0

    # variables like damage and others that this ability might use
    dmg = 0
    self_dmg = 0

    def __init__(self):
        pass

    def action(self, combat, caster, casted):

        bonus_damage = 0
        for index in range(0, caster.combat_level["brawler"]):
            bonus_damage += 5

        base_dmg = (15 + (.15 * caster.dmg) + bonus_damage)
        damage.deal(combat, caster, casted, base_dmg, False, 0, 0, self.style)

        # only deal damage to yourself if you actually landed a hit
        if damage.get_mitigated_value() > 0:
            dialogue.dia(None, f"{caster.name}{colors.LightRed} just hurt themselves for {damage.get_mitigated_value() * .1} damage!{colors.Reset}")
            caster.hp -= damage.get_mitigated_value() * .1

    # if this move is only used once, deal an extra 10 damage.
    def special(self, combat, caster, casted):

        # see how many dev punches we did
        count = 0
        for ability in combat.swings:
            if ability.name == self.name:
                count += 1

        # weapon class check, player and enemy have them in different locations
        weapon_class = ""
        if caster.type == "player":
            weapon_class = caster.equipped[0].wclass
        else:
            weapon_class = caster.wclass

        # checking if combat.swings == 0 is basically checking to see if your turn is over before applying.
        if count == 1 and combat.swing == 0 and self.cur_cd <= 0 and weapon_class == "brawling":
            self.cur_cd = self.cooldown

            dialogue.dia(None, f"\n{caster.name} has gotten {self.name}'s special, {colors.Magenta}and has dealt {colors.LightMagenta}10 {colors.Magenta}extra damage with their brawling weapon!{colors.Reset}")

            casted.hp -= 10
