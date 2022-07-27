from time import sleep

from Items.Materials.wolf_pelt import wolf_pelt
from Items.Weapons.rusty_iron_sword import rusty_iron_sword
from Saves.save_and_load import save_and_load
from Utility.colors import colors
from Utility.dialogue import dialogue
from Utility.equipment import equipment
from Utility.list_check import list_check


class wolf_pelts_for_everyone(object):

    name = "Wolf Pelts for Everyone!"
    desc = "Bjorne heard that the local Blacksmith needs more Wolf Pelts for the kingdom. He wants you to get 3 pelts for the kingdom."

    starting = 0

    type = "quest"

    lvl_req = 0
    location = "Stronia"

    @staticmethod
    def can_do_quest(player):
        if player.level >= wolf_pelts_for_everyone.lvl_req and wolf_pelts_for_everyone not in player.completed_quests and wolf_pelts_for_everyone.name not in list_check.names(player.current_quests):
            return 1

        return 0

    # runs through the starting protocol, this only gets called on once and is called on by the questgiver when accepting a quest for the first time
    def start(self, player, questgiver):
        dialogue.dia(questgiver.name, "I overheard the Blacksmith talk about needing more Wolf Pelts yesterday... he sounded a bit frustrated! You should help him out and get 3 Wolf Pelts.")

    # when you check a quest in the menu, this method is called
    def check(self, player):

        pelt_count = 0
        for item in equipment.compressed_inv:
            if item.name == wolf_pelt.name:
                pelt_count += equipment.compressed_inv[wolf_pelt]

        if pelt_count >= 3:
            self.give_reward(player)
            player.returning(0)

        else:
            print(f"{colors.Red}\nYou don't have enough Wolf Pelts! You need 3 Pelts.{colors.Reset}")
            sleep(2)
            player.returning(0)

    # gives the quest reward
    # need to use this method because we do not want to differentiate between reward types.
    def give_reward(self, player):

        print("\n")
        dialogue.dia(None, "You go to the Blacksmith and find a donation box for Wolf Pelts. It is empty. You put your three Wolf Pelts in the box, and begin to leave.")
        dialogue.dia(f"{colors.Blue}???{colors.Reset}", "Wait!")
        dialogue.dia(None, "You quickly look around.")
        dialogue.dia(f"{colors.LightYellow}Blacksmith{colors.Reset}", "You've been the only one to donate these Wolf Pelts.")
        dialogue.dia(player.name, "Yeah... I see that.")
        dialogue.dia(f"{colors.LightYellow}Blacksmith{colors.Reset}", "Let me give you something!")
        dialogue.dia(player.name, "Is that... how a donation works?")
        dialogue.dia(f"{colors.LightYellow}Blacksmith{colors.Reset}", "I don't care! Let me show you my gratitude.")

        equipment.add_to_inv(rusty_iron_sword)

        player.completed_quests.append(wolf_pelts_for_everyone)

        # delete the wolf pelts
        equipment.del_item(wolf_pelt)
        equipment.del_item(wolf_pelt)
        equipment.del_item(wolf_pelt)

        # delete the quest from current quests
        for index in range(0, len(player.current_quests)):
            if player.current_quests[index] == self:
                del player.current_quests[index]
                break

        save_and_load.save(player)
        dialogue.dia(None, f"{colors.LightGreen}Your game has been saved.{colors.Reset}")
