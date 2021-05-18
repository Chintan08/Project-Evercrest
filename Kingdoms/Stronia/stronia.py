from Characters.Questgivers.bjorne import bjorne
from Core.menus import *
from Kingdoms.Stronia.fort_anvil import fort_anvil
from Utility.equipment import equipment
from Utility.combat import combat
from Utility.shop import shop
from Utility.crafting import craft
from Utility.dialogue import dialogue
from Items.Weapons.wooden_sword import wooden_sword
from Characters.Masters.kaero import kaero
from Enemies.Stronia.golagmite import golagmite

from Kingdoms.Stronia.barren_land import barren_land


class stronia:
    name = "Stronia"
    discovered = False
    desc = f"\n{fore.CYAN_1}A once grand kingdom, shrunken down by its old wars. Now, it resides in the Stronia " \
           f"Mountain " \
           f"Valley, its citizens forging the greatest items known to Evercrest.{style.RESET}\n"
    type = "location"

    tier = 0
    location = 0
    travel = {}
    call = False

    wep_inv = [wooden_sword]
    helm_inv = []
    chest_inv = []
    leg_inv = []
    boot_inv = []
    acc_inv = []
    mat_inv = []

    shop_options = {1: wep_inv, 2: helm_inv, 3: chest_inv, 4: leg_inv, 5: boot_inv, 6: acc_inv, 7: mat_inv}

    def __init__(self, player):
        self.player = player

    def menu_prompt(self):

        # we tell player that you can now return here when return is called with input of 0.
        self.player.returning(self)
        equipment.check_for_none()

        # is kingdom discovered?
        if not self.discovered:
            print(
                f"{fore.CYAN_1}\nYou enter the Stronia Mountain Valley and find yourself looking at a giant, stone fort wall. Behind "
                f"it, you see many forgers metalworking. You are in Stronia.{style.RESET}")

            self.player.lexicon.update_discovery(self)

        quests = []
        for quest in self.player.current_quests:
            if quest.location is self.name:
                quests.append(quest)

        list = [f"Visit {colors.Magenta}Bjorne, the Gossiper{colors.Reset}",
                f"Visit {colors.LightMagenta}Master Kaero{colors.Reset}",
                f"Enter the {colors.Red}Wilds{colors.Reset} of {colors.Yellow}Stronia{colors.Reset}",
                f"View your {colors.Blue}Lexicon{colors.Reset}",
                f"Manage your {colors.Cyan}equipment and inventory{colors.Reset}",
                f"Visit the {colors.Green}Market{colors.Reset}",
                f"{colors.Yellow}Craft{colors.Reset} something",
                f"Leave {colors.Yellow}Stronia{colors.Reset}"]

        if len(quests) > 0:
            list += [quest.name for quest in quests]

        ans = gen_menu_enum(
            f"What would you like to do in {colors.Yellow}{self.name}{colors.Reset}, {self.player.name}?",
            list,
            "What would you like to do?", 0)

        if ans == 1:
            self.town_quest()

        if ans == 2:
            self.master()

        if ans == 3:
            self.wilds()

        if ans == 4:
            self.player.lexicon.view_prompt()

        if ans == 5:
            equipment.equip_prompt()

        if ans == 6:
            shop.shop(0, self.shop_options, self.player)

        if ans == 7:
            craft.crafting(self.player)

        if ans == 8:
            self.player.return_to_world(0)

        if ans in range(9, len(list)+1):
            quests[ans - 9].start(self.player)

    def town_quest(self):
        print("\n")

        if not bjorne.discovered:

            dialogue.dia(bjorne.name, f"You come to me for a quest?")
            self.player.lexicon.update_discovery(bjorne)

        if self.player.level >= bjorne.quests[0].lvl_req and not bjorne.quests[0].completed and bjorne.quests[0] not in self.player.current_quests:

            dialogue.dia(None, bjorne.quests[0].undiscovered_desc)
            self.player.current_quests.append(bjorne.quests[0])
            self.player.lexicon.update_discovery(bjorne.quests[0])
            bjorne.quests[0].start(self.player)

        dialogue.dia(bjorne.name, "I haven't heard much else. Now, go!")
        self.menu_prompt()

    def master(self):

        if not kaero.discovered:
            dialogue.dia(None, "You come across an alcove, and see a Terranox mediating on the cliffside.")
            dialogue.dia(self.player.name, "Who are you?")
            dialogue.dia(f"{colors.LightBlue}???{colors.Reset}", "Hm? You do not know?")
            dialogue.dia(None,
                         "You are surprised he did not fling you off the mountain for interrupting his meditation.")
            dialogue.dia(self.player.name, "No, I'm new here. Are you an Ability Master?")
            dialogue.dia(f"{colors.LightBlue}???{colors.Reset}",
                         f"At least you know that much. I am {kaero.name}, the Ability Master for Stronia.")

            self.player.lexicon.update_discovery(kaero)

            dialogue.dia(kaero.name,
                         "I can teach you all about Brawling and heavier attacks, but you have to prove to me that you can fight.")
            dialogue.dia(kaero.name,
                         "Prove that to me by fighting off different enemies around Evercrest, and come back to me.")

        # CINDERBLADE
        # check if the ability is not discovered, check if the enemy is in self.player.enemies_killed, then check how many have been killed, and then check the level

        if kaero.abilities[0].discovered is False and golagmite.name in self.player.enemies_killed and self.player.enemies_killed[golagmite.name] >= 1 and self.player.level >= 1:

            dialogue.dia(kaero.name, f"I think you are ready to learn {kaero.abilities[0].name}.")
            equipment.add_to_inv(kaero.abilities[0])

            dialogue.dia(kaero.name, f"Use this wisely.")

            self.master()  # go back to kaero and see if there's more to learn

        dialogue.dia(kaero.name,
                     "There's not much I can teach you right now. Come back later if you think you are ready.")
        self.menu_prompt()

    def wilds(self):

        if self.tier in range(0, 11):
            self.location = barren_land

        elif self.tier in range(11, 21):
            self.location = fort_anvil

        # if the amount of locations you have is less than two, we will not ask you where to go
        if len(self.travel) < 2:
            pass

        # call is a boolean that is needed to make sure you do not get prompted again every time you call on the Wilds
        # when you leave the Wilds, call is set to False
        # But until you quit, you will only get this prompt ONCE, unless your travel size is less than 1
        else:

            if not self.call:
                self.call = True

                ans = gen_menu_num("Where would you like to travel to?\n",
                                   [self.travel[travel].name for travel in self.travel] + ["Back"],
                                   "Where would you like to go?", 0)

                if ans != len(self.travel) + 1:
                    self.location = self.travel[ans]
                    self.tier = self.location.min_tier
                    print(f"You are now travelling to {colors.Cyan}{self.location.name}{colors.Reset}!\n")

                else:
                    self.call = False
                    self.player.returning(0)

            else:
                pass

        if not self.location.discovered:
            print(self.location.undiscovered_desc)
            self.player.lexicon.update_discovery(self.location)

            self.travel[len(self.travel) + 1] = self.location

        # pick boss if in boss tier
        #if self.tier in (9, 19, 29, 39, 49):
            #enemy = self.location.boss[0]

        # pick enemy if not in boss tier
        #else:
        enemy = self.location.pick_enemy()

        # main wilds loop, will continue running until leaving
        while True:

            victory = combat.precheck(self.player, enemy)

            if victory:
                self.tier += 1

                print(
                    f"\n{colors.Green}Congrats!{colors.Reset} You defeated {colors.Red}{enemy.name}{colors.Reset}, and you get to move on in the Wilds. {colors.Blue}You are now at Tier {colors.Yellow}{self.tier}{colors.Reset}{colors.Blue}!{colors.Reset}")

                ans = gen_menu_num(
                    f"You can either {colors.Green}continue{colors.Reset}, or {colors.Red}leave{colors.Reset}. What do you want to do?",
                    [f"{colors.Green}Continue{colors.Reset}", f"{colors.Red}Leave{colors.Reset}"], "What do you do?", 0)

                # if you leave
                if ans == 2:
                    self.call = False
                    self.tier = 0
                    self.player.returning(0)

                # if you stay
                else:
                    self.call = True
                    self.wilds()

            # if you lost
            elif not victory:

                self.tier = 0
                self.call = False

                print("\nSomeone came and brought you to the Stronia medical tent, and healed you back up.\n")
                self.player.returning(0)
