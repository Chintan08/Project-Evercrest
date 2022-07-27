

# predict your opponent's 3rd swing style
from Utility.colors import colors
from Utility.dialogue import dialogue


class prediction:

    # variables like damage and hp and duration, values should be 0 except for dur
    style = None
    swings = 0
    duration = 1

    caster = None
    casted = None

    # how many times can this effect stack
    stack = 2

    # this typing makes it so effects of the same type do NOT stack
    type = "prediction"

    # last few variables should be the same amount of variables above
    def __init__(self, combat, caster, casted, style, swings):

        self.style = style
        self.swings = swings
        self.caster = caster
        self.casted = casted

        # run the initial phase
        self.initial(combat)

    # what runs on start
    def initial(self, combat):
        dialogue.dia(None, f"{self.caster.name} is making a prediction on your third swing! If they guess correctly, they gain an extra swing!")

    # called from combat once effect is appended from ability
    def constant(self, combat):

        # subtract duration after effect constant runs, then see if it needs to be reverted
        self.duration -= 1
        if self.duration <= 0:
            self.revert(combat)

    # kills the effect, but can do other things on revert
    def revert(self, combat):

        # style.style is the string form of the name of the style
        if len(combat.swings) == 3 and combat.swings[2].style.style == self.style.style:
            dialogue.dia(None, f"{self.casted.name} predicted {colors.LightGreen}correctly{colors.Reset}! They have gained an extra swing!")

            heal = 0
            for level in range(0, self.caster.combat_level["duelist"]):
                heal += 0.02

            if self.caster.combat_level["duelist"] > 0:
                dialogue.dia(None, f"{self.caster.name} also healed for {heal * self.caster.maxhp} HP!")
                self.caster.hp += heal * self.caster.maxhp

            combat.swing += 1

        else:
            dialogue.dia(None, f"{self.casted.name} predicted {colors.LightRed}incorrectly{colors.Reset}! They have taken {int(self.casted.maxhp * .15)} damage!")
            self.casted.hp -= int(self.casted.maxhp * .15)

        combat.kill_effect()
