from Utility.colors import colors
from Utility.dialogue import dialogue


class ignite:

    # variables like damage and hp and duration, values should be 0 except for dur
    bonus_damage = 0
    duration = 3

    caster = None
    casted = None

    # how many times can this effect stack
    stack = 1

    # this typing makes it so effects of the same type do NOT stack
    type = "ignite"

    # last few variables should be the same amount of variables above
    def __init__(self, combat, caster, casted, bonus_damage, duration):

        self.bonus_damage = bonus_damage
        self.duration = duration
        self.caster = caster
        self.casted = casted

        # run the initial phase
        self.initial(combat)

    # what runs on start
    def initial(self, combat):

        dialogue.dia(None, f"{self.caster.name} is {colors.LightRed}Ignited{colors.Reset} for {self.duration} rounds. They will gain {self.bonus_damage} damage while ignited.")
        self.caster.dmg += 10

    # called from combat once effect is appended from ability
    def constant(self, combat):

        # subtract duration after effect constant runs, then see if it needs to be reverted
        self.duration -= 1
        if self.duration <= 0:
            self.revert(combat)

    # kills the effect, but can do other things on revert
    def revert(self, combat):

        dialogue.dia(None, f"{self.caster.name}'s fire from the Ignition has died down.")
        self.caster.dmg -= 10
        combat.kill_effect()
