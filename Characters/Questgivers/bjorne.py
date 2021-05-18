from Quests.Stronia.golagmite_infestation import golagmite_infestation
from Utility.colors import colors


class bjorne:

    name = f"{colors.Magenta}Bjorne{colors.Reset}"
    desc = "An infamous gossiper of Stronia. As much as people don't like him, though, he is a very useful person.\n" \
           "He is the questgiver of Stronia. Go to him if you want to embark on more adventures."

    type = "character"
    discovered = False

    quests = [golagmite_infestation]