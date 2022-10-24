from Utility.colors import colors
from Utility.damage import damage
from Utility.dialogue import dialogue

# deals flat damage, but ignores any armor percentage, damage increases off of standard stacks, reduces flat armor by eldric
class duelist:

    type = "style"
    style = "duelist"
    name = f"{colors.Magenta}Duelist{colors.Reset}"
    desc = f"\nA Duelist Combo will deal flat damage, but ignores your Armor%.\n" \
           f"{colors.Magenta}Enhancers{colors.Reset}:\n" \
           f"Standard: Increases the flat damage by 15 for each Standard count.\n" \
           f"Eldric: Reduces the flat armor of an opponent by 25 for each Eldric style.\n" \
           f"{colors.Yellow}Level Bonus: Deal an extra 5 base damage for each Duelist level{colors.LightYellow}\n"

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

        bonus_damage = 0
        for level in range(0, caster.combat_level["duelist"]):
            bonus_damage += 5

        base_dmg = 15 + bonus_damage
        standard_dmg = 15 * s_count
        eldric_cut = 25 * e_count

        dmg = int((base_dmg + standard_dmg) - (casted.armor - eldric_cut))

        if dmg > 0:
            print(f"{colors.LightBlue}{caster.name}{colors.Reset} dealt {colors.Yellow}{dmg}{colors.Reset} damage to {colors.LightRed}{casted.name}{colors.Reset}!")
            casted.hp -= dmg

            # we store the damage of this ability in the value dictionary the damage class has because it is used for XP distribution, this normally is done in damage.deal()
            damage.add_to_values(caster, duelist.style, dmg)

        else:
            print(f"{colors.LightBlue}{caster.name}{colors.Red} could not get past {colors.LightRed}{casted.name}{colors.Reset}'s defense!\n")

        dialogue.dia(None, f"\n{colors.LightMagenta}{caster.name} has performed a {duelist.name} {colors.LightMagenta}Combo!{colors.Reset}")


