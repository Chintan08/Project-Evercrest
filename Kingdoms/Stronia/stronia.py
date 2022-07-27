from Characters.Questgivers.bjorne import bjorne
from Core.menus import *
from Items.Accessories.dry_ward import dry_ward
from Items.Armor.Boots.rustic_boots import rustic_boots
from Items.Armor.Chestplates.rustic_chestplate import rustic_chestplate
from Items.Armor.Helmets.rustic_helmet import rustic_helmet
from Items.Armor.Leggings.rustic_leggings import rustic_leggings
from Items.Weapons.rusty_iron_sword import rusty_iron_sword
from Kingdoms.Stronia.fort_anvil import fort_anvil
from Kingdoms.Stronia.heart_of_stronia import heart_of_stronia
from Kingdoms.Stronia.the_canyon import the_canyon
from Kingdoms.Stronia.the_deep_prisons import the_deep_prisons
from Saves.save_and_load import save_and_load
from Utility.equipment import equipment
from Utility.combat import combat
from Utility.shop import shop
from Utility.crafting import craft
from Utility.dialogue import dialogue
from Items.Weapons.wooden_sword import wooden_sword
from Characters.Masters.kaero import kaero

from Kingdoms.Stronia.barren_land import barren_land


class stronia:

    name = "Stronia"

    # TODO: change these descriptions
    undiscovered_desc = f"{colors.Cyan}\nYou enter the Stronia Mountain Valley and find yourself looking at a giant, stone fort wall. Behind it, you see many forgers metalworking. You are in Stronia.{colors.Reset}"
    world_desc = f"\nStronia is the home to the greatest metal workers of all time.\n"
    desc = f"\n{colors.Cyan}A once grand kingdom, shrunken down by its old wars. Now, it resides in the Stronia " \
           f"Mountain " \
           f"Valley, its citizens forging the greatest items known to Evercrest.{colors.Reset}\n"

    type = "location"

    tier = 0
    location = 0
    call = False

    # SHOP ITEMS
    wep_inv = [wooden_sword, rusty_iron_sword]
    helm_inv = [rustic_helmet]
    chest_inv = [rustic_chestplate]
    leg_inv = [rustic_leggings]
    boot_inv = [rustic_boots]
    acc_inv = [dry_ward]
    mat_inv = []

    shop_options = {1: wep_inv, 2: helm_inv, 3: chest_inv, 4: leg_inv, 5: boot_inv, 6: acc_inv, 7: mat_inv}

    def __init__(self, player):
        self.player = player

    def menu_prompt(self):

        # we tell player that you can now return here when return is called with input of 0.
        self.player.returning(self)
        equipment.check_for_none()

        # is kingdom discovered?
        self.player.lexicon.update_discovery(stronia)

        quests = []
        for quest in self.player.current_quests:
            if quest.location is self.name:
                quests.append(quest)    # used only in stronia

        list = [f"Visit {colors.Magenta}Bjorne, the Gossiper{colors.Reset}",
                f"Visit {colors.LightMagenta}Master Kaero{colors.Reset}",
                f"Enter the {colors.Red}Wilds{colors.Reset} of {colors.Yellow}Stronia{colors.Reset}",
                f"View your {colors.Blue}Lexicon{colors.Reset}",
                f"Manage your {colors.Cyan}equipment and inventory{colors.Reset}",
                f"Visit the {colors.Green}Market{colors.Reset}",
                f"{colors.Yellow}Craft{colors.Reset} something",
                f"Leave {colors.Yellow}Stronia{colors.Reset}",
                f"{colors.LightGreen}Save{colors.Reset} your game"]

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

        if ans == 9:
            save_and_load.save(self.player)
            dialogue.dia(None, f"{colors.LightGreen}Saving your game... and done!{colors.Reset}")
            self.player.returning(0)

        if ans in range(10, len(list) + 1):
            quests[ans - 10].check(self.player)

    def town_quest(self):

        bjorne.give_quest(self.player)
        self.menu_prompt()

    def master(self):

        kaero.give_ability(self.player)
        self.menu_prompt()

    def wilds(self):

        locations = [barren_land, the_canyon, fort_anvil, the_deep_prisons, heart_of_stronia]
        travel = {}

        for place in locations:
            if self.player.lexicon.is_discovered(place):
                travel[len(travel) + 1] = self.location

        if self.tier in range(0, 10):
            self.location = barren_land

        elif self.tier in range(10, 20):
            self.location = the_canyon

        elif self.tier in range(20, 30):
            self.location = fort_anvil

        elif self.tier in range(30, 40):
            self.location = the_deep_prisons

        else:
            self.location = heart_of_stronia

        # if the amount of locations you have is less than two, we will not ask you where to go
        if len(travel) < 2:
            pass

        # call is a boolean that is needed to make sure you do not get prompted again every time you call on the Wilds
        # when you leave the Wilds, call is set to False
        # But until you quit, you will only get this prompt ONCE, unless your travel size is less than 1
        else:

            if not self.call:
                self.call = True

                ans = gen_menu_num("Where would you like to travel to?\n",
                                   [travel[area].name for area in travel] + ["Back"],
                                   "Where would you like to go?", 0)

                if ans != len(travel) + 1:
                    self.location = travel[ans]
                    self.tier = self.location.min_tier
                    print(f"You are now travelling to {colors.Cyan}{self.location.name}{colors.Reset}!\n")

                else:
                    self.call = False
                    self.player.returning(0)

            else:
                pass

        self.player.lexicon.update_discovery(self.location)

        travel[len(travel) + 1] = self.location

        # pick boss if in boss tier
        if self.tier in (9, 19, 29, 39, 49):
            enemy = self.location.pick_boss()

        # pick enemy if not in boss tier
        else:
            enemy = self.location.pick_enemy()

        # main wilds loop, will continue running until leaving
        while True:

            victory = combat.precheck(self.player, enemy)

            if victory:

                self.tier += 1

                # heal player by 25% of their maxhp if they win
                self.player.hp += (.25 * self.player.maxhp)
                if self.player.hp > self.player.maxhp:
                    self.player.hp = self.player.maxhp

                dialogue.dia(None, f"\n{colors.Green}Congrats!{colors.Reset} You defeated {colors.Red}{enemy.name}{colors.Reset}, and you get to move on in the Wilds. {colors.Blue}You are now at Tier {colors.Yellow}{self.tier}{colors.Reset}{colors.Blue}!{colors.Reset}")

                dialogue.dia(None, f"\nYou have healed {colors.LightGreen}{.25 * self.player.maxhp}{colors.Reset} health.")

                ans = gen_menu_num(
                    f"You can either {colors.Green}continue{colors.Reset}, or {colors.Red}leave{colors.Reset}. What do you want to do?",
                    [f"{colors.Green}Continue{colors.Reset}", f"{colors.Red}Leave{colors.Reset}"], "What do you do?", 0)

                # if you leave
                if ans == 2:
                    self.call = False
                    self.tier = 0
                    self.player.hp = self.player.maxhp
                    self.player.returning(0)

                # if you stay
                else:
                    self.call = True
                    self.wilds()

            # if you lost
            elif not victory:

                self.tier = 0
                self.call = False

                dialogue.dia(None,
                             "\nSomeone came and brought you to the Stronia medical tent, and healed you back up.\n")
                self.player.returning(0)
