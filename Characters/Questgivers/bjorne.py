from Quests.Stronia.The_Admirer.chasing_your_admirer import chasing_your_admirer
from Quests.Stronia.The_Admirer.luxurious_rockington_inn import luxurious_rockington_inn
from Quests.Stronia.distressing_grayed_bull import distressing_grayed_bull
from Quests.Stronia.golagmite_infestation import golagmite_infestation
from Quests.Stronia.wolf_pelts_for_everyone import wolf_pelts_for_everyone
from Utility.colors import colors
from Utility.dialogue import dialogue


class bjorne:

    name = f"{colors.Magenta}Bjorne{colors.Reset}"
    desc = "An infamous gossiper of Stronia. As much as people don't like him, though, he is a very useful person.\n" \
           "He is the quest giver of Stronia. Go to him if you want to embark on more adventures."

    type = "character"

    quests = [golagmite_infestation, wolf_pelts_for_everyone, distressing_grayed_bull, luxurious_rockington_inn, chasing_your_admirer]

    @staticmethod
    def give_quest(player):
        quest = None

        # checks if discovered
        if not player.lexicon.is_discovered(bjorne):
            print("\n")
            dialogue.dia(bjorne.name, f"You come to me for a quest?")
            player.lexicon.update_discovery(bjorne)

        # GOLAGMITE INFESTATION #
        if bjorne.quests[0].can_do_quest(player):

            quest = bjorne.quests[0]()
            quest.start(player, bjorne)
            player.current_quests.append(quest)
            player.lexicon.update_discovery(bjorne.quests[0])

        # WOLF PELTS FOR EVERYONE #
        if bjorne.quests[1].can_do_quest(player):

            quest = bjorne.quests[1]()
            quest.start(player, bjorne)
            player.current_quests.append(quest)
            player.lexicon.update_discovery(bjorne.quests[1])

        # THE DISTRESSING GRAYED BULL #
        if bjorne.quests[2].can_do_quest(player):

            quest = bjorne.quests[2]()
            quest.start(player, bjorne)
            player.current_quests.append(quest)
            player.lexicon.update_discovery(bjorne.quests[2])

        # THE LUXURIOUS ROCKINGTON INN (THE ADMIRER 1/4) #
        if bjorne.quests[3].can_do_quest(player):

            quest = bjorne.quests[3]()
            quest.start(player, bjorne)
            player.current_quests.append(quest)
            player.lexicon.update_discovery(bjorne.quests[3])

        # CHASING YOUR ADMIRER (THE ADMIRER 2/4) #
        if bjorne.quests[4].can_do_quest(player):

            quest = bjorne.quests[4]()
            quest.start(player, bjorne)
            player.current_quests.append(quest)
            player.lexicon.update_discovery(bjorne.quests[4])

        dialogue.dia(bjorne.name, "Surprisingly, I haven't heard much else. Now scram!")
        player.returning(0)
