from Utility.colors import colors


# cuts through a percentage of the enemy's flat armor, does extra hp damage with brawler, flat armor through resolute
class elitist:

    type = "style"
    style = "elitist"
    name = f"{colors.LightRed}Elitist{colors.Reset}"
    desc = f"An Elitist Combo cuts through a percentage of the enemy's flat armor.\n" \
           f"{colors.Magenta}Enhancers{colors.Reset}:\n" \
           f"Brawler: Does extra damage after armor penetration.\n" \
           f"Resolute: Reduces the amount of flat armor even further.\n"
    discovered = False

    @staticmethod
    def action(combat, caster, casted):
        b_count = 0
        r_count = 0

        for style in combat.styles:

            if style.style == "brawler":
                b_count+=1

            if style.style == "resolute":
                r_count+=1

        base_cut = casted.armor - (.1*casted.armor)
        base_damage = 20
        brawler_damage = 30 * b_count
        resolute_cut = (5 * r_count)

        casted_armor = (casted.armor - base_cut) - resolute_cut
        damage = base_damage + brawler_damage
        dmg = int((damage * (1 - casted.armor_percent)) - casted_armor)

        if dmg > 0:
            casted.hp -= dmg
            print(f"{colors.LightMagenta}{caster.name} has performed a {elitist.name} {colors.LightMagenta}Combo!{colors.Reset}")
            print(f"{caster.name} has cut through {1-casted_armor} armor, and dealt {damage} damage to {casted.name}!")
        else:
            print(f"{caster.name} could not break through {casted.name}'s armor!")

        casted.hp -= int((damage * (1 - casted.armor_percent)) - casted_armor)
