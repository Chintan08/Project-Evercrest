from Utility.colors import colors
from Items.Abilities.cinderblade import cinderblade


class kaero:

    name = f"{colors.LightYellow}Master Kaero{colors.Reset}"
    desc = "A massive, menacing Terranox who coincidentally is also an ability master located in Stronia." \
           "\nHe teaches heavy combat and a little bit on how to brawl with your fists."

    type = "character"

    discovered = False

    abilities = [cinderblade]