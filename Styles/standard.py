from Utility.colors import colors


# does flat damage, increases base damage with duelist and percentage maxhp with eldric
class standard:

    type = "style"
    style = "standard"
    name = f"{colors.White}Standard{colors.Reset}"
    desc = f"A Standard Combo will deal flat damage to your opponent.\n" \
           f"{colors.Magenta}Enhancers{colors.Reset}:\n" \
           f"Eldric: Increases MaxHP damage.\n" \
           f"Duelist: Increases flat damage.\n"
    discovered = False

    @staticmethod
    def action(combat, caster, casted):
        # these variables are the amount of times a style of an enhancer has occurred
        e_count = 0
        d_count = 0

        for style in combat.styles:

            if style.style == "duelist":
                d_count += 1

            if style.style == "eldric":
                e_count += 1

        # at base level, deal 30% of your damage
        base_dmg = 15 + (.3 * caster.dmg)
        # for every brawler stack deal extra 10
        duelist_count = d_count * 10
        # for every eldric count, deal 5% of the enemy's maxhp
        eldric_percent = (.05*e_count) * casted.maxhp

        dmg = int(((base_dmg + duelist_count + eldric_percent) * (1-casted.armor_percent)) - casted.armor)

        print(f"{colors.LightMagenta}{caster.name} has performed a {standard.name} {colors.LightMagenta}Combo!{colors.Reset}")

        if dmg > 0:
            casted.hp -= dmg
            print(f"{caster.name} dealt {colors.LightYellow}{dmg}{colors.Reset} damage to {casted.name}!")
        else:
            print(f"{caster.name} could not break through {casted.name}'s armor!")

        # 100 - (15 - ((.3 * 20) + (1 * 10) + (((.05 * 1) * 100)))) = 51
