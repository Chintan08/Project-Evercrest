from Utility.colors import colors


# deals flat damage, but ignores any armor percentage, damage increases off of standard stacks, reduces flat armor by eldric
class duelist:

    type = "style"
    style = "duelist"
    name = f"{colors.Magenta}Duelist{colors.Reset}"
    desc = f"A Duelist Combo will deal flat damage, but ignores your Armor%.\n" \
           f"{colors.Magenta}Enhancers{colors.Reset}:\n" \
           f"Standard: Increases the flat damage.\n" \
           f"Eldric: Reduces any flat armor..\n"
    discovered = False

    @staticmethod
    def action(combat, caster, casted):
        # these variables are the amount of times a style of an enhancer has occurred
        e_count = 0
        s_count = 0

        for style in combat.styles:

            if style.style == "standard":
                s_count += 1

            if style.style == "eldric":
                e_count += 1

        base_dmg = 15
        standard_dmg = 15 * s_count
        eldric_cut = 5 * e_count

        dmg = int((base_dmg + standard_dmg) - (casted.armor - eldric_cut))

        print(
            f"{colors.LightMagenta}{caster.name} has performed a {duelist.name} {colors.LightMagenta}Combo!{colors.Reset}")

        if dmg > 0:
            casted.hp -= dmg
            print(f"{caster.name} dealt {colors.LightYellow}{dmg}{colors.Reset} damage to {casted.name}!")
        else:
            print(f"{caster.name} could not break through {casted.name}'s armor!")


