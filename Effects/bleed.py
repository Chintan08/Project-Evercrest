from Utility.colors import colors

# bleeds are incredibly scary; they can stack more than once and deal incredible amounts of damage.
from Utility.dialogue import dialogue


class bleed:

    # variables like damage and hp and duration
    dmg = 0

    duration = 0

    caster = None
    casted = None

    # how many times can this effect stack
    stack = 4

    # this typing makes it so effects of the same type do NOT stack
    type = "bleed"

    # last few variables should be the same amount of variables above
    def __init__(self, combat, caster, casted, dmg, duration):
        self.dmg = dmg
        self.duration = duration
        self.caster = caster
        self.casted = casted

        # run the initial phase
        self.initial(combat)

    # what runs on start
    def initial(self, combat):

        dialogue.dia(None, f"{colors.Red}{self.casted.name} is bleeding for {colors.LightRed}{self.dmg}{colors.Red} damage which will last {colors.LightRed}{self.duration}{colors.Red} rounds.{colors.Reset}")

    # called from combat once effect is appended from ability
    def constant(self, combat):
        self.casted.hp -= self.dmg
        dialogue.dia(None, f"\n{self.casted.name} just {colors.Red}bled{colors.Reset} for {colors.LightRed}{self.dmg} damage.{colors.Reset}")

        # subtract duration after effect constant runs, then see if it needs to be reverted
        self.duration -= 1
        if self.duration <= 0:
            self.revert(combat)

    # kills the effect, but can do other things on revert
    def revert(self, combat):

        dialogue.dia(None, f"The bleeding has stopped for {self.casted.name}.")
        combat.kill_effect()
