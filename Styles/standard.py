from Utility.colors import colors


# does flat damage, increases base damage with duelist and percentage maxhp with eldric
from Utility.damage import damage
from Utility.dialogue import dialogue


class standard:

    type = "style"
    style = "standard"
    name = f"{colors.White}Standard{colors.Reset}"
    desc = f"A Standard Combo will deal flat damage to your opponent.\n" \
           f"\n{colors.Magenta}Enhancers{colors.Reset}:\n" \
           f"Eldric: Increases MaxHP damage.\n" \
           f"Duelist: Increases flat damage.\n" \
           f"{colors.Yellow}Level Bonus: Deal an extra base 5 damage per Standard level{colors.LightYellow}\n"

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

        # for every duelist stack deal extra 20
        duelist_count = d_count * 20

        # for every eldric count, deal 5% of the enemy's maxhp
        eldric_percent = (.05*e_count) * casted.maxhp

        # standard level bonus
        bonus_damage = 0
        for index in range(0, caster.combat_level["standard"]):
            bonus_damage += 5

        dmg = int(base_dmg + duelist_count + eldric_percent + bonus_damage)

        dialogue.dia(None, f"\n{colors.LightMagenta}{caster.name} has performed a {standard.name} {colors.LightMagenta}Combo!{colors.Reset}")

        damage.deal(combat, caster, casted, dmg, False, 0, 0, standard)

