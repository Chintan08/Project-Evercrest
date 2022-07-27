from time import sleep

from Saves.save_and_load import save_and_load
from Utility.colors import colors
from Enemies.Stronia.baby_golagmite import baby_golagmite
from Utility.dialogue import dialogue
from Utility.list_check import list_check


class golagmite_infestation(object):

    name = "Golagmite Infestation"
    desc = "Bjorne has heard that there have been heavy Golagmite Infestations. Clean out 2 of them."

    starting = 0

    type = "quest"

    lvl_req = 0
    location = "Stronia"

    def __init__(self):
        pass

    @staticmethod
    def can_do_quest(player):

        if player.level >= golagmite_infestation.lvl_req and golagmite_infestation not in player.completed_quests and golagmite_infestation.name not in list_check.names(player.current_quests):
            return 1

        return 0

    def start(self, player, questgiver):

        dialogue.dia(questgiver.name, "The People of Stronia have been getting mad at the Baby Golagmites running rampant. Help them out.")

        if baby_golagmite.name not in player.enemies_killed:
            self.starting = 0

        else:
            self.starting = player.lexicon.compress_kills()[baby_golagmite.name]

    def check(self, player):

        if baby_golagmite.name not in player.enemies_killed:
            print(f"\n{colors.Red}You haven't killed a single Baby Golagmite!{colors.Reset}\n")
            sleep(2)
            player.returning(0)

        elif player.lexicon.compress_kills()[baby_golagmite.name] - self.starting >= 3:
            self.give_reward(player)
            player.returning(0)

        else:
            print(f"\n{colors.LightRed}You haven't killed enough Baby Golagmites...{colors.Reset}\n")
            sleep(2)
            player.returning(0)

    # gives the quest reward
    # need to use this method because we do not want to differentiate between reward types.
    def give_reward(self, player):

        print(f"\nYou've been given {colors.Green}$50{colors.Reset} dollars for your hard work.\n")
        sleep(1)
        player.money += 50

        player.completed_quests.append(golagmite_infestation)

        for index in range(0, len(player.current_quests)):
            if player.current_quests[index] == self:
                del player.current_quests[index]
                break

        save_and_load.save(player)
        dialogue.dia(None, f"{colors.LightGreen}Your game has been saved.{colors.Reset}")
