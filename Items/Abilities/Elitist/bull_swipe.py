from Effects.exhausted import exhausted
from Styles.elitist import elitist
from Utility.colors import colors
from Utility.damage import damage
from Utility.dialogue import dialogue


class bull_swipe:

    type = "ability"

    # import the style of the ability
    style = elitist

    # +1
    cooldown = 8

    name = f"{colors.LightRed}Bull Swipe{colors.Reset}"
    desc = f"Mimic the swipe of a Bull's Horn using your blade. This attack is incredibly strong if you have the power. This ability can not crit." \
           f"\n{colors.Magenta}Type: {colors.LightMagenta}{style.name}{colors.Reset}" \
           f"\n{colors.Blue}Special: {colors.LightBlue}If used first, forfeit all swings and swipe again, but it is enhanced. Each swing consumed adds another swipe's worth of damage to the swipe." \
           f"\nBecome Exhausted, slowing yourself by 6 speed for 4 turns.{colors.Reset}" \
           f"\n{colors.Green}Special Cooldown: {colors.LightGreen}{cooldown-1} Rounds" \
           f"\n{colors.Red}Damage: {colors.LightRed}45% of your damage." \
           f"\n{colors.Yellow}Level Bonus: {colors.LightYellow}Increase % of your damage by 3% for each Elitist level.{colors.Reset}"

    cur_cd = 0

    # variables like damage and others that this ability might use
    dmg = 0
    self_dmg = 0
    bonus_damage = 0

    def __init__(self):
        pass

    def action(self, combat, caster, casted):

        self.bonus_damage = 0
        for index in range(0, caster.combat_level["elitist"]):
            self.bonus_damage += .03

        base_dmg = (.45 + self.bonus_damage) * caster.dmg
        damage.deal(combat, caster, casted, base_dmg, False, 0, 0, self.style)

    def special(self, combat, caster, casted):

        if self.cur_cd <= 0 and combat.swings[0].name == bull_swipe.name:

            self.cur_cd = self.cooldown
            dialogue.dia(None, f"\n{caster.name} has gotten {self.name}'s special, {colors.Magenta}and has swiped again with incredible ferocity!{colors.Reset}")

            combat.styles.append(self.style)
            combat.swings.append(self)

            # for each swing consumed add extra damage to an empowered swing
            dmg = int(5 + ((.5 + self.bonus_damage) * caster.dmg))
            total_dmg = dmg
            for index in range(1, combat.swing):
                total_dmg += dmg

            damage.deal(combat, caster, casted, total_dmg, False, 0, 0, self.style)
            combat.swing = 0

            self.check_effect(combat, caster, caster)

    def check_effect(self, combat, caster, casted):

        effect_count = 0
        for effect in combat.effects[casted.type]:

            if effect.type == exhausted.type:
                effect_count += 1

        if effect_count < exhausted.stack:  # changes how many times this effect can stack
            combat.effects[casted.type].append(exhausted(combat, caster, casted, 6, 4))
