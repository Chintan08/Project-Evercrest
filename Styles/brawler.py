from Utility.colors import colors
from Effects.bleed import bleed


# leaves you with a bleeding effect, with the severity increasing with elitist, and duration increasing with nimbilic
class brawler:

    type = "style"
    style = "brawler"
    name = f"{colors.Red}Brawler{colors.Reset}"
    desc = f"A Brawler Combo that leaves the opponent with a bleeding effect.\n" \
           f"{colors.Magenta}Enhancers{colors.Reset}:\n" \
           f"Elitist: Severity of the bleed increases.\n" \
           f"Nimbilic: Increases the duration of the bleed.\n"

    discovered = False

    @staticmethod
    def action(combat, caster, casted):
        # these variables are the amount of times a style of an enhancer has occurred
        n_count = 0
        d_count = 0

        for style in combat.styles:

            if style.style == "nimbilic":
                n_count += 1

            if style.style == "elitist":
                d_count += 1

        # 15 base tick damage
        base_dmg = 15
        # duration of 2
        base_duration = 2

        elitist_damage = 15 * d_count
        nimbilic_duration = 1 * n_count

        print(
            f"{colors.LightMagenta}{caster.name} has performed a {brawler.name} {colors.LightMagenta}Combo!{colors.Reset}\n")

        effect_count = 0
        for effect in combat.effects[casted.type]:

            if effect.type == bleed.type:
                effect_count += 1

        if effect_count < bleed.stack:  # changes how many times this effect can stack
            combat.effects[casted.type].append(bleed(combat, caster, casted, (base_dmg + elitist_damage), (base_duration + nimbilic_duration)))


