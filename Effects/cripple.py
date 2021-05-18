from Utility.colors import colors


class cripple:

    # variables like damage and hp and duration
    dmg_reduc = 0.0
    spd_reduc = 0.0
    arm_reduc = 0.0
    arm_pen_reduc = 0.0
    duration = 2

    # how many times can this effect stack
    stack = 1

    # this typing makes it so effects of the same type do NOT stack
    type = "cripple"

    damage = 0.0
    speed = 0.0
    armor = 0.0
    armor_percent = 0.0

    # last few variables should be the same amount of variables above
    def __init__(self, combat, caster, casted, dmg, spd, arm, arm_pen):

        self.dmg_reduc = dmg
        self.spd_reduc = spd
        self.arm_reduc = arm
        self.arm_pen_reduc = arm_pen

        # run the initial phase
        self.initial(combat, caster, casted)

    # what runs on start
    def initial(self, combat, caster, casted):
        print(f"{colors.LightRed}{casted.name}{colors.Red} has been {colors.LightRed}Crippled!{colors.Red}")

        # how much you took away
        self.damage = casted.dmg*self.dmg_reduc
        self.speed = casted.speed*self.spd_reduc
        self.armor = casted.armor*self.arm_reduc
        self.armor_percent = casted.armor_percent*self.arm_pen_reduc

        # apply effect
        casted.dmg *= (1-self.dmg_reduc)
        casted.speed *= (1-self.spd_reduc)
        casted.armor *= (1-self.arm_reduc)
        casted.armor_percent *= (1-self.arm_pen_reduc)

    # called from combat once effect is appended from ability
    def constant(self, combat, caster, casted):

        # subtract duration after effect constant runs, then see if it needs to be reverted
        self.duration -= 1
        if self.duration <= 0:
            self.revert(combat, caster, casted)

    # kills the effect, but can do other things on revert
    def revert(self, combat, caster, casted):

        casted.dmg += self.damage
        casted.speed += self.speed
        casted.armor += self.armor
        casted.armor_percent += self.armor_percent

        print(f"\n{colors.LightBlue}{casted.name} is no longer Crippled.{colors.Reset}\n")
        combat.kill_effect()
