
from Enemies.Stronia.rockington_bandit import rockington_bandit
from Items.Abilities.Brawling.dev_strike import dev_strike
from Kingdoms.Stronia.rockington_inn import rockington_inn
from Saves.save_and_load import save_and_load
from Utility.colors import colors
from Utility.combat import combat
from Utility.dialogue import dialogue
from Utility.equipment import equipment
from Utility.list_check import list_check


class luxurious_rockington_inn(object):

    name = "The Luxurious Rockington Inn"
    desc = "You've been invited to the Rockington Inn to sleep for free, by a secret admirer! What could go wrong?\n" \
           f"Quest Line: {colors.LightGreen}The Admirer (1/4){colors.Reset}"

    type = "quest"

    lvl_req = 3
    location = "Stronia"

    qname = ""

    @staticmethod
    def can_do_quest(player):

        if player.level >= luxurious_rockington_inn.lvl_req and luxurious_rockington_inn not in player.completed_quests and luxurious_rockington_inn.name not in list_check.names(player.current_quests):
            return 1

        return 0

    def start(self, player, questgiver):

        self.qname = questgiver.name

        dialogue.dia(questgiver.name, "Where do you sleep?")
        dialogue.dia(player.name, "I have a sleeping bag. I just bounce around places.")
        dialogue.dia(questgiver.name, "It seems like someone knew that already. I've been asked to extend an act of gratitude to you.")
        dialogue.dia(player.name, "By who?")
        dialogue.dia(questgiver.name, "I do not know. Perhaps by an admirer? You've done great things for Stronia so far, I'd be surprised if no one thanked you.")
        dialogue.dia(questgiver.name, "You've been given a special room in the Rockington Inn to sleep for free for a few nights!")
        dialogue.dia(player.name, "Woah; Rockington Inn? That place is crazy nice! And expensive...")
        dialogue.dia(questgiver.name, "I would take it if I were you.")
        dialogue.dia(player.name, "I will. Thanks!")

    def check(self, player):

        if not player.lexicon.is_discovered(rockington_inn):

            player.lexicon.update_discovery(rockington_inn)

            dialogue.dia(None, "You walk up to the inn keeper, to ask for your room.")
            dialogue.dia("Inn Keeper", "Ah yes! It seems you have an Admirer upon your hands. Right this way!")
            dialogue.dia(None, "You follow the Inn Keeper to your room, and are blown away by the soft bed, dressing tables, and all that has gone into the room. You have been given a special room.")
            dialogue.dia("Inn Keeper", "Enjoy!")

        dialogue.dia(None, "Hours have passed as you've gotten comfortable in your room. With nothing equipped and kept far away, for once, you feel at ease.")
        dialogue.dia(None, "Suddenly, a bandit barges into your room! A massive grin is on his face, and you quickly realize this was an ambush!")
        dialogue.dia(None, "You ball up your fists; you will have to fight this Bandit with nothing equipped.")

        for item in player.equipped:
            equipment.deequip_item(item, True)

        victory = combat.precheck(player, rockington_bandit(40, 7, 12, 0.02, 3))

        if victory:
            dialogue.dia(None, "As you pummel the Bandit, you quickly grab your equipment and leave.")
            dialogue.dia(None, "As you run through the Inn and outside, you notice that no one heard anything. You give the Inn keeper a death stare, and they smile back. They didn't know what happened.")
            dialogue.dia(None, "Thankfully for you, the Bandit came dressed with a uniform. The uniform was unique; it had an emblem. Now, it's time for you to find your Admirer with that emblem.")

            player.hp = player.maxhp
            self.give_reward(player)
            player.returning(0)

        else:
            player.hp = player.maxhp
            player.returning(0)

    # gives the quest reward
    # need to use this method because we do not want to differentiate between reward types.
    def give_reward(self, player):

        equipment.add_to_inv(dev_strike)
        player.give_combat_xp(dev_strike.style, 25)

        player.completed_quests.append(luxurious_rockington_inn)

        for index in range(0, len(player.current_quests)):
            if player.current_quests[index] == self:
                del player.current_quests[index]
                break

        save_and_load.save(player)
        dialogue.dia(None, f"{colors.LightGreen}Your game has been saved.{colors.Reset}")
