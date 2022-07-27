from Utility.colors import colors


# cuts through a percentage of the enemy's flat armor, does extra hp damage with brawler, flat armor through resolute
from Utility.damage import damage
from Utility.dialogue import dialogue


class elitist:

    type = "style"
    style = "elitist"
    name = f"{colors.LightRed}Elitist{colors.Reset}"
    desc = f"\nAn Elitist Combo cuts through 25% of the enemy's flat armor.\n" \
           f"{colors.Magenta}Enhancers{colors.Reset}:\n" \
           f"Brawler: Does extra damage after armor penetration.\n" \
           f"Resolute: Reduces the amount of flat armor even further." \
           f"{colors.Yellow}Level Bonus: Increases the base damage dealt by 5 for each Elitist level{colors.LightYellow}\n\n"

    # TODO: elitist level bonus
    @staticmethod
    def action(combat, caster, casted):
        b_count = 0
        r_count = 0

        for style in combat.styles:

            if style.style == "brawler":
                b_count+=1

            if style.style == "resolute":
                r_count+=1

        bonus_damage = 0
        for level in range(0, caster.combat_level["elitist"]):
            bonus_damage += 5

        base_cut = casted.armor - (.25*casted.armor)
        base_damage = 15 + bonus_damage
        brawler_damage = 30 * b_count
        resolute_cut = (5 * r_count)

        casted_armor = (casted.armor - base_cut) - resolute_cut

        dmg = int((base_damage + brawler_damage * (1 - casted.armor_percent)) - casted_armor)

        dialogue.dia(None, f"\n{colors.LightMagenta}{caster.name} has performed an {elitist.name} {colors.LightMagenta}Combo!{colors.Reset}")

        if dmg > 0:
            print(f"{colors.LightBlue}{caster.name}{colors.Reset} dealt {colors.Yellow}{dmg}{colors.Reset} damage to {colors.LightRed}{casted.name}{colors.Reset}!")
            casted.hp -= dmg

            # we store the damage of this ability in the value dictionary the damage class has because it is used for XP distribution, this normally is done in damage.deal()
            damage.add_to_values(caster, elitist.style, dmg)

        else:
            print(f"{colors.LightBlue}{caster.name}{colors.Red} could not get past {colors.LightRed}{casted.name}{colors.Reset}'s defense!\n")



