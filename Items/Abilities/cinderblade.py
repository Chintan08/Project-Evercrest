from Utility.colors import colors
from Styles.eldric import eldric
from Effects.burn import burn

class cinderblade:

    type = "ability"
    style = eldric

    discovered = False

    name = f"{colors.Red}Cinderblade{colors.Reset}"
    desc = f"Sets your enemy on fire." \
           f"\n{colors.Magenta}Type:{colors.LightMagenta}{style.name}{colors.Reset}"

    # +1
    cooldown = 3
    cur_cd = 0

    dmg = 15

    def __init__(self):

        dmg = self.dmg
        cur_cd = self.cur_cd
        cooldown = self.cooldown

    def action(self, combat, caster, casted):

        base_dmg = int(10 + (.45 * caster.dmg))
        self.dmg = (base_dmg * (1 - casted.armor_percent)) - casted.armor

        if self.dmg > 0:
            print(f"{colors.LightBlue}{caster.name}{colors.Reset} dealt {colors.Yellow}{self.dmg}{colors.Reset} damage to {colors.LightRed}{casted.name}{colors.Reset}!\n")
            casted.hp -= self.dmg

        else:
            print(f"{colors.LightBlue}{caster.name}{colors.Red} could not get past {colors.LightRed}{casted.name}{colors.Reset}'s defense!\n")

        # when applying an effect, check to see if there are no duplicates
        self.check_effect(combat, caster, casted)

    def special(self, combat, caster, casted):

        count = 0
        for ability in combat.swings:
            if ability == self.name:
                count+=1

        if count == 3 and self.cur_cd <= 0:
            self.cur_cd = self.cooldown

            print(f"\n{caster.name} has gotten {self.name}'s special, and has casted it once more time.")
            combat.styles.append(self.style)
            self.action(combat, caster, casted)

    # use this method ONLY if this ability applies an effect
    def check_effect(self, combat, caster, casted):

        effect_count = 0
        for effect in combat.effects[casted.type]:

            if effect.type == burn.type:
                effect_count += 1

        if effect_count < burn.stack: # changes how many times this effect can stack
            combat.effects[casted.type].append(burn(combat, caster, casted, 1, 3))