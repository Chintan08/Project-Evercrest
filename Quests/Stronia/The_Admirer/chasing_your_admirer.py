from Enemies.Stronia.mountain_vulture_bandit_rookie import mountain_vulture_bandit_rookie
from Items.Weapons.bandit_scimitar import bandit_scimitar
from Kingdoms.Stronia.southern_mountain_vulture_camp import southern_mountain_vulture_camp
from Quests.Stronia.The_Admirer.luxurious_rockington_inn import luxurious_rockington_inn
from Saves.save_and_load import save_and_load
from Styles.standard import standard
from Utility.colors import colors
from Utility.combat import combat
from Utility.dialogue import dialogue
from Utility.equipment import equipment
from Utility.list_check import list_check


class chasing_your_admirer(object):

    name = "Chasing your Admirer"
    desc = "After the events at Rockington Inn, you now have an idea of where the ambush came from. You recall a bandit camp that sports this emblem, so your first stop is there.\n" \
           f"Quest Line: {colors.LightGreen}The Admirer (2/4){colors.Reset}"

    type = "quest"

    lvl_req = 3
    location = "Stronia"

    qname = ""

    @staticmethod
    def can_do_quest(player):

        if player.level >= chasing_your_admirer.lvl_req and chasing_your_admirer not in player.completed_quests and chasing_your_admirer not in list_check.names(player.current_quests) and luxurious_rockington_inn in player.completed_quests:
            return 1

        return 0

    def start(self, player, questgiver):

        luxurious_rockington_inn.qname = questgiver.name

        dialogue.dia(player.name, "Bjorne! You set me up!")
        dialogue.dia(questgiver.name, "What?")
        dialogue.dia(player.name, "The Rockington Ambush! Did you know?")
        dialogue.dia(questgiver.name, "No! You got ambushed? By who?")
        dialogue.dia(player.name, "By some bandits.")
        dialogue.dia(None, "You describe the emblem the Bandit wore.")
        dialogue.dia(questgiver.name, "Ah... the Mountain Vultures! They're notorious around here. They must think you're a threat.")
        dialogue.dia(player.name, "Where can I find them?")
        dialogue.dia(questgiver.name, "You can find them beyond the Southern Gate. Good luck, though; there are a lot of Vulture Rookies sitting around.")
        dialogue.dia(player.name, "Thanks.")

    def check(self, player):

        if not player.lexicon.is_discovered(southern_mountain_vulture_camp):

            player.lexicon.update_discovery(southern_mountain_vulture_camp)

        dialogue.dia(None, "You see the main gate is guarded. However, you look around the perimeter and find a smaller, unguarded entrance.")
        dialogue.dia(None, "Your goal is to do as much damage as possible and extract information. You spot a Bandit, and it becomes your first target.")

        dialogue.dia(None, f"{colors.LightYellow}This is a {colors.LightGreen}Non-Survival{colors.LightYellow} quest. This means you will fully heal after every fight.{colors.Reset}")

        victory = combat.precheck(player, mountain_vulture_bandit_rookie(50, 8, 15, 0.02, 1))

        if victory:
            dialogue.dia(player.name, "I got ambushed by you guys! Who was responsible?!")
            dialogue.dia("Bandit Rookie", "Uhh, we just do what the chief does!")
            dialogue.dia(player.name, "Where is the chief?!")
            dialogue.dia("Bandit Rookie", "Uh, uh, wh- who?")
            dialogue.dia(None, "Angry, you quickly kill him. No good information will come out of him. You go to find the next target.")

            player.hp = player.maxhp

        else:
            player.hp = player.maxhp
            player.returning(0)

        dialogue.dia(None, "You spot a rogue Bandit Rookie. You quickly approach him and get ready to fight.")

        victory = combat.precheck(player, mountain_vulture_bandit_rookie(50, 10, 17, 0.02, 2))

        if victory:
            dialogue.dia(player.name, "Where can I find your chief?!")
            dialogue.dia("Bandit Rookie", "Uhh... he's at another camp!")
            dialogue.dia(player.name, "Which one?!")
            dialogue.dia("Bandit Rookie", "I don't know?! Why does everyone think I know things? It's my first day!")
            dialogue.dia(None, "Angry, you quickly kill him. No good information will come out of him. You go to find the next target.")

            player.hp = player.maxhp

        else:
            player.hp = player.maxhp
            player.returning(0)

        dialogue.dia(None, "You find the only other Bandit Rookie alone. You jump him.")

        victory = combat.precheck(player, mountain_vulture_bandit_rookie(55, 10, 17, 0.02, 1))

        if victory:
            dialogue.dia(player.name, "What camp is your chief at?!")
            dialogue.dia("Bandit Rookie", "He's at... I can't tell you!")
            dialogue.dia(player.name, "Which one?!")
            dialogue.dia("Bandit Rookie", "Okay, Okay! There's one in The Canyon! The Canyon Vulture Camp! That one!")
            dialogue.dia("Bandit Rookie", "Good luck getting in there though! That camp is tight with security!")
            dialogue.dia("Bandit Rookie", "You would need a special uniform from the Red Vulture Camp! Good luck, haha... oh. I wasn't supposed to say that.")
            dialogue.dia(player.name, "Thanks! Now, bye bye.")
            dialogue.dia(None, "You quickly kill the bandit, and leave the scene. No one knew you were here, but they will eventually.")

            player.hp = player.maxhp
            self.give_reward(player)
            player.returning(0)

        else:
            player.hp = player.maxhp
            player.returning(0)

    # gives the quest reward
    # need to use this method because we do not want to differentiate between reward types.
    def give_reward(self, player):

        equipment.add_to_inv(bandit_scimitar)
        player.give_combat_xp(standard, 25)

        player.completed_quests.append(chasing_your_admirer)

        for index in range(0, len(player.current_quests)):
            if player.current_quests[index] == self:
                del player.current_quests[index]
                break

        save_and_load.save(player)
        dialogue.dia(None, f"{colors.LightGreen}Your game has been saved.{colors.Reset}")
