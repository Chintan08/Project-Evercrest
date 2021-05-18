from Utility.colors import colors

# bleeds are incredibly scary; they can stack more than once and deal incredible amounts of damage.
class bleed:

    # variables like damage and hp and duration
    dmg = 0

    duration = 0

    # how many times can this effect stack
    stack = 2

    # this typing makes it so effects of the same type do NOT stack
    type = "bleed"

    # last few variables should be the same amount of variables above
    def __init__(self, combat, caster, casted, dmg, duration):
        self.dmg = dmg
        self.duration = duration

        # run the initial phase
        self.initial(combat, caster, casted)

    # what runs on start
    def initial(self, combat, caster, casted):

        print(f"{colors.Red}{casted.name} is bleeding for {colors.LightRed}{self.dmg}{colors.Red} damage which will last {colors.LightRed}{self.duration}{colors.Red} rounds.{colors.Reset}")

    # called from combat once effect is appended from ability
    def constant(self, combat, caster, casted):
        casted.hp -= self.dmg
        print(f"\n{casted.name} just {colors.Red}bled{colors.Reset} for {colors.LightRed}{self.dmg} damage.{colors.Reset}\n")

        # subtract duration after effect constant runs, then see if it needs to be reverted
        self.duration -= 1
        if self.duration <= 0:
            self.revert(combat, caster, casted)

    # kills the effect, but can do other things on revert
    def revert(self, combat, caster, casted):

        print(f"The bleeding has stopped for {casted.name}.")
        combat.kill_effect()
