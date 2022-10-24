from Utility.colors import colors


# heals you for flat hp, increases flat hp increase with Duelist, and percentage missing hp with brawler
from Utility.dialogue import dialogue


class resolute:

    type = "style"
    style = "resolute"
    name = f"{colors.LightGreen}Resolute{colors.Reset}"
    desc = f"A Resolute Combo will heal you for certain amounts of HP.\n" \
           f"\n{colors.Magenta}Enhancers{colors.Reset}:\n" \
           f"Duelist: Increases the amount of Flat HP gained by 40 for each Duelist style.\n" \
           f"Brawler: Increases the amount of HP from Missing HP by 12.5% for each Brawler style.\n" \
           f"{colors.Yellow}Level Bonus: Heal an extra 5 HP per Resolute level{colors.LightYellow}\n"

    @staticmethod
    def action(combat, caster, casted):
        # these variables are the amount of times a style of an enhancer has occurred
        d_count = 0
        b_count = 0

        for style in combat.styles:

            if style.style == "brawler":
                b_count += 1

            if style.style == "duelist":
                d_count += 1

        bonus_healing = 0
        for level in range(0, caster.combat_level["resolute"]):
            bonus_healing += 5

        # at base level, heal 10 hp
        base_hp = 10 + bonus_healing

        # for every duelist count gain an extra 40 hp
        duelist_count = 40 * d_count

        # for every brawler count, gain 12.5% of your missing hp back
        brawler_percent = (.125*b_count) * (caster.maxhp - caster.hp)

        healing = base_hp + duelist_count + brawler_percent
        dialogue.dia(None, f"\n{colors.LightMagenta}{caster.name} has performed a {resolute.name} {colors.LightMagenta}Combo!{colors.Reset}\n{caster.name} has healed {healing} HP back.")

        caster.hp += healing
        if caster.hp > caster.maxhp:
            caster.hp = caster.maxhp
