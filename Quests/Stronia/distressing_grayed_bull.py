from time import sleep

from Enemies.Stronia.Bosses.gray_bull import gray_bull
from Utility.save_and_load import save_and_load
from Utility.colors import colors
from Utility.dialogue import dialogue
from Utility.list_check import list_check


class distressing_grayed_bull(object):

    name = "The Distressing Grayed Bull"
    desc = "The Grayed Bull is a threat to anyone who wants to go through The Canyon. Bjorne thinks you're strong enough to take on the Bull; do you?"

    type = "quest"

    lvl_req = 3
    location = "Stronia"

    qname = ""

    @staticmethod
    def can_do_quest(player):

        if player.level >= distressing_grayed_bull.lvl_req and distressing_grayed_bull not in player.completed_quests and distressing_grayed_bull.name not in list_check.names(player.current_quests):
            return 1

        return 0

    def start(self, player, questgiver):

        self.qname = questgiver.name

        dialogue.dia(None, "You approach Bjorne, and you see him staring at you, as if he is studying you.")
        dialogue.dia(questgiver.name, "Hm...")
        dialogue.dia(player.name, "What?")
        dialogue.dia(questgiver.name, "Have you heard of the 'Distressing' Grayed Bull?")

        if player.lexicon.is_discovered(gray_bull):
            dialogue.dia(player.name, "Yeah! I've ran into that abomination before. What about it?")
        else:
            dialogue.dia(player.name, "No. Why, what's up?")

        dialogue.dia(questgiver.name, "The bull is the naturally elected guardian of The Canyon. The Canyon was once a big trading route we used; but now, the Bull stands in the way.")
        dialogue.dia(player.name, "Is the Canyon not dangerous?")
        dialogue.dia(questgiver.name, "... We'll get to that another day.")
        dialogue.dia(questgiver.name, "People want that Bull gone. But soldiers are too busy not doing soldier things, and no one is man enough to face the Bull. But I think you are.")
        dialogue.dia(player.name, "... Oh. You know, I don't think- ")
        dialogue.dia(questgiver.name, "I think you're perfect. And I've elected you! Go! Make Stronia proud for 10 seconds, before you realize The Canyon is even worse!")

    def check(self, player):

        if gray_bull.name in player.enemies_killed:

            dialogue.dia(self.qname, "You did it?!")
            dialogue.dia(player.name, "Yeah! That was... rough. But I did it!")
            dialogue.dia(self.qname, "The people of Stronia want to pay you for it. Here you go!")
            self.give_reward(player)
            player.returning(0)

        else:
            print(f"{colors.Red}You haven't killed a single Grayed Bull!{colors.Reset}")
            sleep(1)
            player.returning(0)

    # gives the quest reward
    # need to use this method because we do not want to differentiate between reward types.
    def give_reward(self, player):

        print(f"\nYou've been given {colors.Green}$300{colors.Reset} dollars for your hard work.\n")
        sleep(1)
        player.money += 300

        player.completed_quests.append(distressing_grayed_bull)

        for index in range(0, len(player.current_quests)):
            if player.current_quests[index] == self:
                del player.current_quests[index]
                break

        save_and_load.save(player)
        dialogue.dia(None, f"{colors.LightGreen}Your game has been saved.{colors.Reset}")
