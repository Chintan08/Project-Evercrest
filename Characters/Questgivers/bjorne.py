from Quests.Stronia.The_Admirer.chasing_your_admirer import chasing_your_admirer
from Quests.Stronia.The_Admirer.luxurious_rockington_inn import luxurious_rockington_inn
from Quests.Stronia.distressing_grayed_bull import distressing_grayed_bull
from Quests.Stronia.golagmite_infestation import golagmite_infestation
from Quests.Stronia.wolf_pelts_for_everyone import wolf_pelts_for_everyone
from Utility.colors import colors
from Utility.dialogue import dialogue


class bjorne:

    name = f"{colors.Magenta}Bjorne{colors.Reset}"
    desc = "No one knows who Bjorne is. Where he comes from, where he lives, what he does, is unknown.\n" \
           "What is known though, is his passion to listen in on everyone's conversations! This may also be why no one really likes him." \
           f"While his gossip skills are annoying, they are useful to you. With him, you'll be able to embark on many quests in Stronia."

    type = "character"

    quests = [golagmite_infestation, wolf_pelts_for_everyone, distressing_grayed_bull, luxurious_rockington_inn, chasing_your_admirer]

    @staticmethod
    def give_quest(player):
        quest = None

        # checks if discovered
        if not player.lexicon.is_discovered(bjorne):
            print("\n")
            dialogue.dia(None, f"As you turn the corner of a marketplace, you come across a small, white-bearded man sitting against the wall, all scrunched up.")
            dialogue.dia(player.name, "I'm sorry... are you homeless?")
            dialogue.dia(f"{colors.LightBlue}???{colors.Reset}", "WHAT?! No!")
            dialogue.dia(None, "His eyes flare up at you. But when he got a better look at you, his eyes became normal.")
            dialogue.dia(f"{colors.LightBlue}???{colors.Reset}", "I know you! I've heard about you already, some odd traveler.")
            dialogue.dia(player.name, "Who are you?")
            dialogue.dia(f"{colors.LightBlue}???{colors.Reset}", f"I am {bjorne.name}! And I am probably going to be your new best friend!")

            player.lexicon.update_discovery(bjorne)

            dialogue.dia(player.name, "How so?")
            dialogue.dia(bjorne.name, "I have ears that listen to all of Stronia! And you are an adventurer! I can give you adventures while you stay in Stronia!")
            dialogue.dia(player.name, "Okay... I'll let you know if I'm bored. Or something like that.")
            dialogue.dia(bjorne.name, f"Perfect! You'd be surprised how much I know.")

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
