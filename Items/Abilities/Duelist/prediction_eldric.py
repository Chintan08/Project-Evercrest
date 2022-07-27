from Effects.prediction import prediction
from Styles.duelist import duelist
from Styles.eldric import eldric
from Utility.colors import colors
from Utility.dialogue import dialogue


class prediction_eldric:

    type = "ability"

    # import the style of the ability
    style = duelist

    # +1
    cooldown = 9

    name = f"{colors.LightMagenta}Prediction: Eldric{colors.Reset}"
    desc = f"A good duelist studies their opponent. When they are confident, they predict your next move. And if they're right, they suddenly become confident enough to strike even harder.\n" \
           f"Predict your opponent's third swing style. If it is a Eldric ability, gain an extra swing on your next turn. If you've guessed wrong, take damage equal to 15% of your maxHP. This goes on cooldown for 4 turns." \
           f"When you enter combat, the name will be {colors.LightMagenta}Obscured{colors.Reset}. You will not see the prediction type, and neither will your opponent." \
           f"\n{colors.Magenta}Type: {colors.LightMagenta}{style.name}{colors.Reset}" \
           f"\n{colors.Blue}Special: {colors.LightBlue}If used first, forfeit all swings and double down. If you've guessed correctly, gain 2 swings on your next turn. If you're wrong, take damage equal to 35% of your maxHP.{colors.Reset}" \
           f"\n{colors.Green}Special Cooldown: {colors.LightGreen}{cooldown-1} Rounds" \
           f"\n{colors.Yellow}Level Bonus: {colors.LightYellow}Heal 2% of your maxHP for each Duelist Level.{colors.Reset}"

    cur_cd = 0
    action_cd = 0

    # variables like damage and others that this ability might use
    dmg = 0
    self_dmg = 0

    round_called = 0

    def __init__(self):
        self.name = f"{colors.LightMagenta}Prediction: ???{colors.Reset}"

    def action(self, combat, caster, casted):

        # because actions can't be live updated, we do math to find out how many rounds have passed
        if self.action_cd == 0:
            self.round_called = combat.round
        else:
            if combat.round - self.round_called == 4:
                self.action_cd = 0

        # checks if you're faster according to the game
        if combat.mobs[0] == caster and self.action_cd == 0:
            self.action_cd = 4

            self.check_effect(combat, caster, caster)

        elif self.action_cd != 0:
            dialogue.dia(None, f"{caster.name} tried making a prediction, but it's still on cooldown!")

        else:

            dialogue.dia(None, f"{caster.name} tried making a prediction, but they're too slow!")

    def special(self, combat, caster, casted):

        if self.cur_cd <= 0 and combat.swings[0].name == prediction_eldric.name and combat.swing != 0 and combat.mobs[0] == caster:

            self.cur_cd = self.cooldown
            dialogue.dia(None, f"\n{caster.name} has gotten {self.name}'s special, {colors.Magenta}and is Doubling Down!{colors.Reset}")

            combat.swing = 0
            self.check_effect(combat, caster, caster)

    def check_effect(self, combat, caster, casted):

        effect_count = 0
        for effect in combat.effects[casted.type]:

            if effect.type == prediction.type:
                effect_count += 1

        if effect_count < prediction.stack:  # changes how many times this effect can stack
            combat.effects[casted.type].append(prediction(combat, caster, casted, eldric, 1))
