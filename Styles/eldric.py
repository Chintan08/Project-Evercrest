from Utility.colors import colors
from Effects.cripple import cripple

# A combo that applies a Cripple. Crippling cuts their dmg, armor, armor%, and speed for 2 rounds. Resolute increases dmg and speed cripple, Nimbilic increases armor and armor% cripple.
from Utility.dialogue import dialogue


class eldric:

    type = "style"
    style = "eldric"
    name = f"{colors.LightMagenta}Eldric{colors.Reset}"
    desc = f"An Eldric Combo will cripple your opponent, reducing Damage, Armor% and Armor, and Speed for two rounds.\n" \
           f"\n{colors.Magenta}Enhancers{colors.Reset}:\n" \
           f"Resolute: Increases Damage and Speed Cripple by 8% and 5% respectively.\n" \
           f"Nimbilic: Increases Armor and Armor% Cripple by 5% and 2% respectively.\n" \
           f"{colors.Yellow}Level Bonus: Increases the Damage cripple by 2% for each Eldric level{colors.LightYellow}\n"

    @staticmethod
    def action(combat, caster, casted):
        # these variables are the amount of times a style of an enhancer has occurred
        n_count = 0
        r_count = 0

        for style in combat.styles:

            if style.style == "resolute":
                r_count += 1

            if style.style == "nimbilic":
                n_count += 1

        bonus_damage = 0
        for level in range(0, caster.combat_level["eldric"]):
            bonus_damage += .02

        dmg_cripple = .15 + (r_count * .08) + bonus_damage
        spd_cripple = .1 + (r_count * .05)
        arm_cripple = .05 + (n_count * .05)
        arm_pen_cripple = .01 + (n_count * .02)

        dialogue.dia(None, f"\n{colors.LightMagenta}{caster.name} has performed an {eldric.name} {colors.LightMagenta}Combo!{colors.Reset}")

        effect_count = 0
        for effect in combat.effects[casted.type]:

            if effect.type == cripple.type:
                effect_count += 1

        if effect_count < cripple.stack:  # changes how many times this effect can stack
            combat.effects[casted.type].append(
                cripple(combat, caster, casted, dmg_cripple, spd_cripple, arm_cripple, arm_pen_cripple))
