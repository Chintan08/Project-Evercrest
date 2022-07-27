from Utility.colors import colors
from Styles.eldric import eldric
from Effects.burn import burn
from Utility.damage import damage
from Utility.dialogue import dialogue


class cinderblade:

    type = "ability"
    style = eldric

    # +1
    cooldown = 3

    name = f"{colors.Red}Cinderblade{colors.Reset}"
    desc = f"Uses the body of your enemy to spark a fire on the blade, burning your opponent and dealing damage." \
           f"\n{colors.Magenta}Type: {colors.LightMagenta}{style.name}{colors.Reset}" \
           f"\n{colors.Blue}Special: {colors.LightBlue}When {name}{colors.LightBlue} is used 3 times, it is used a fourth time." \
           f"\n{colors.Green}Special Cooldown: {colors.LightGreen}{cooldown-1} Rounds" \
           f"\n{colors.Red}Damage: {colors.Red}10 + 45% of your damage." \
           f"\n{colors.Green}Effect: {colors.LightRed}Burns {colors.LightGreen}your opponent for 1 damage for 3 turns. Does not work if your opponent is immune to fire." \
           f"\n{colors.Yellow}Level Bonus: {colors.LightYellow}"

    cur_cd = 0

    dmg = 15

    def __init__(self):
        pass

    # TODO: change this ability or at least care about it more, this is a stab copy and paste with a burn effect when it really shouldn't be
    def action(self, combat, caster, casted):

        bonus_damage = 0
        for index in range(0, caster.eldric_level):
            bonus_damage += 10

        base_dmg = int(10 + (.45 * caster.dmg) + bonus_damage)
        damage.deal(combat, caster, casted, base_dmg, False, 0, 0, self.style)

        # when applying an effect, check to see if there are no duplicates
        self.check_effect(combat, caster, casted)

    def special(self, combat, caster, casted):

        count = 0
        for ability in combat.swings:
            if ability.name == self.name:
                count += 1

        # TODO: change this special condition and special to reflect cinderblade better
        if count == 3 and self.cur_cd <= 0:
            self.cur_cd = self.cooldown

            dialogue.dia(None, f"\n{caster.name} has gotten {self.name}'s special, and has casted it once more time.")
            combat.styles.append(self.style)
            combat.swings.append(self)
            self.action(combat, caster, casted)

    # use this method ONLY if this ability applies an effect
    def check_effect(self, combat, caster, casted):

        effect_count = 0
        for effect in combat.effects[casted.type]:

            if effect.type == burn.type:
                effect_count += 1

        if effect_count < burn.stack: # changes how many times this effect can stack
            combat.effects[casted.type].append(burn(combat, caster, casted, 1, 3))