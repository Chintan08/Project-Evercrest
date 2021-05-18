from Utility.colors import colors


# uses advantages you walk in with
# heals you for flat hp, increases flat hp increase with Duelist, and percentage missing hp with brawler
class resolute:

    type = "style"
    style = "resolute"
    name = f"{colors.LightGreen}Resolute{colors.Reset}"
    desc = f"A Resolute Combo will heal you for certain amounts of HP.\n" \
           f"{colors.Magenta}Enhancers{colors.Reset}:\n" \
           f"Duelist: Increases the amount of Flat HP gained.\n" \
           f"Brawler: Increases the amount of HP from Missing HP.\n"

    discovered = False


    @staticmethod
    def action(combat, caster, casted):
        # these variables are the amount of times a style of an enhancer has occurred
        e_count = 0
        b_count = 0

        for style in combat.styles:

            if style.style == "brawler":
                b_count += 1

            if style.style == "duelist":
                e_count += 1

        # at base level, heal 20 hp
        base_hp = 20
        # for every elitist count gain an extra 40 hp
        elitist_count = 40 * e_count
        # for every brawler count, gain 12.5% of your missing hp back
        brawler_percent = (.125*b_count) * (caster.maxhp - caster.hp)

        healing = base_hp + elitist_count + brawler_percent
        print(f"{colors.LightMagenta}{caster.name} has performed a {resolute.name} {colors.LightMagenta}Combo!{colors.Reset}\n {caster.name} has healed {healing} HP back.")

        caster.hp += healing
        if caster.hp > caster.maxhp:
            caster.hp = caster.maxhp
