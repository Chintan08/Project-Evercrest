from Utility.colors import colors
from Utility.dialogue import dialogue


class burn:

    damage = 0
    duration = 0
    stack = 1

    caster = None
    casted = None

    type = "burn"

    def __init__(self, combat, caster, casted, damage, duration):
        self.damage = damage
        self.duration = duration
        self.caster = caster
        self.casted = casted
        self.initial(combat)

    def initial(self, combat):

        if self.casted.fire_resistance == 1:
            dialogue.dia(None, f"{colors.Magenta}{self.casted.name}{colors.Magenta} was about to be {colors.Red}burned{colors.Magenta}, but they are immune to {colors.Red}Burns!{colors.Reset}")

        else:
            dialogue.dia(None, f"{colors.LightRed}{self.casted.name}{colors.LightRed} has a burn that deals {self.damage * (1 - self.casted.fire_resistance)} damage for {self.duration} rounds!{colors.Reset}")

    def constant(self, combat):

        # checks for burn again because the effect cannot kill itself in initial, due to the way abilities apply effects after initial is done running, not before.
        if self.casted.fire_resistance == 1:
            self.duration = 0
            combat.kill_effect()

        else:
            self.casted.hp -= self.damage * (1 - self.casted.fire_resistance)
            dialogue.dia(None, f"{colors.LightRed}{self.casted.name}{colors.Red} has been burned for {colors.LightRed}{self.damage * (1 - self.casted.fire_resistance)} damage!{colors.Reset}")
            self.duration -= 1

            if self.duration <= 0:
                self.revert(combat)

    def revert(self, combat):

        dialogue.dia(None, f"\n{colors.LightBlue}{self.casted.name} has stopped burning.{colors.Reset}\n")
        combat.kill_effect()
