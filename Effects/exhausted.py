
# reduces speed of casted
from Utility.colors import colors
from Utility.dialogue import dialogue


class exhausted:

    # variables like damage and hp and duration, values should be 0 except for dur
    speed = 0

    duration = 0
    caster = None
    casted = None

    # how many times can this effect stack
    stack = 1

    # this typing makes it so effects of the same type do NOT stack
    type = "exhausted"

    # last few variables should be the same amount of variables above
    def __init__(self, combat, caster, casted, speed, duration):

        self.speed = speed
        self.duration = duration
        self.caster = caster
        self.casted = casted

        # run the initial phase
        self.initial(combat)

    # what runs on start
    def initial(self, combat):
        dialogue.dia(None, f"\n{self.casted.name}{colors.LightCyan} seems a little tired! They are slowed by {self.speed} speed for {self.duration} turns!{colors.Reset}")
        self.casted.speed -= self.speed

    # called from combat once effect is appended from ability
    def constant(self, combat):

        # subtract duration after effect constant runs, then see if it needs to be reverted
        self.duration -= 1
        if self.duration <= 0:
            self.revert(combat)

    # kills the effect, but can do other things on revert
    def revert(self, combat):
        dialogue.dia(None, f"\n{self.casted.name}{colors.LightCyan} got their energy back!{colors.Reset}")
        self.casted.speed += 2

        combat.kill_effect()
