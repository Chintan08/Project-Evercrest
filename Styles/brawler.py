from Utility.colors import colors
from Effects.bleed import bleed
from Utility.dialogue import dialogue

# leaves you with a bleeding effect, with the severity increasing with elitist, and duration increasing with nimbilic
class brawler:

    type = "style"
    style = "brawler"
    name = f"{colors.Red}Brawler{colors.Reset}"
    desc = f"\nA Brawler Combo that leaves the opponent with a bleeding effect.\n" \
           f"{colors.Magenta}Enhancers{colors.Reset}:\n" \
           f"Elitist: Severity of the bleed increases.\n" \
           f"Nimbilic: Increases the duration of the bleed." \
           f"{colors.Yellow}Level Bonus: Increase the damage of the bleed by 3 for each Brawler level{colors.LightYellow}\n\n"

    # TODO: brawler level bonus
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

        bonus_damage = 0
        for level in range(0, caster.combat_level["brawler"]):
            bonus_damage += 3

        elitist_damage = 10 * d_count
        nimbilic_duration = 1 * n_count

        dialogue.dia(None, f"\n{colors.LightMagenta}{caster.name} has performed a {brawler.name} {colors.LightMagenta}Combo!{colors.Reset}")

        effect_count = 0
        for effect in combat.effects[casted.type]:

            if effect.type == bleed.type:
                effect_count += 1

        if effect_count < bleed.stack:  # changes how many times this effect can stack
            combat.effects[casted.type].append(bleed(combat, caster, casted, (base_dmg + elitist_damage + bonus_damage), (base_duration + nimbilic_duration)))


