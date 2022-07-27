from Utility.colors import colors
from Utility.dialogue import dialogue


# poison is similar to burn, but the difference is that it cannot be countered by a resistance
class poison:

    damage = 0
    duration = 0
    stack = 1

    caster = None
    casted = None

    type = "poison"

    def __init__(self, combat, caster, casted, damage, duration):
        self.damage = damage * (1 + caster.poison_amp)
        self.duration = duration
        self.caster = caster
        self.casted = casted
        self.initial(combat)

    def initial(self, combat):

        dialogue.dia(None, f"{colors.LightRed}{self.casted.name}{colors.LightRed} has a poison in their body that deals {self.damage} damage for {self.duration} rounds!{colors.Reset}")

    def constant(self, combat):

        self.casted.hp -= self.damage
        dialogue.dia(None, f"{colors.LightRed}{self.casted.name}{colors.Red}'s poison has hurt them for {colors.LightRed}{self.damage} damage!{colors.Reset}")

        self.duration -= 1

        if self.duration <= 0:
            self.revert(combat)

    def revert(self, combat):

        dialogue.dia(None, f"\n{colors.LightBlue}{self.casted.name} has removed the poison from their body.{colors.Reset}\n")
        combat.kill_effect()
