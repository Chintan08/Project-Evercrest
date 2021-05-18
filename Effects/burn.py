from Utility.colors import colors


class burn:

    damage = 0
    duration = 0
    stack = 1

    type = "burn"

    def __init__(self, combat, caster, casted, damage, duration):
        self.damage = damage
        self.duration = duration
        self.initial(combat, caster, casted)

    def initial(self, combat, caster, casted):

        if casted.can_be_burned is False:
            print(f"{colors.Magenta}{casted.name}{colors.Magenta} was about to be {colors.Red}burned{colors.Magenta}, but they are immune to {colors.Red}Burns!{colors.Reset}")
            combat.kill_effect()

        else:
            print(f"{colors.LightRed}{casted.name}{colors.LightRed} has a burn that deals {self.damage} damage for {self.duration} rounds!{colors.Reset}")

    def constant(self, combat, caster, casted):
        casted.hp -= self.damage
        print(f"{colors.LightRed}{casted.name}{colors.Red} has been burned for {colors.LightRed}{self.damage} damage!{colors.Reset}")
        self.duration -= 1

        if self.duration <= 0:
            self.revert(combat, caster, casted)

    def revert(self, combat, caster, casted):

        print(f"\n{colors.LightBlue}{casted.name} has stopped burning.{colors.Reset}\n")
        combat.kill_effect()
