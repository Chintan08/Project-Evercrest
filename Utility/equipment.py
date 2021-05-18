from Core.menus import *
from Items.Weapons.fists import fists
from Items.Armor.Boots.shoes import shoes
from Items.Armor.Chestplates.shirt import shirt
from Items.Armor.Helmets.no_helmet import no_helmet
from Items.Armor.Leggings.pants import pants
from Items.Accessories.no_accessory import no_accessory
from Items.Abilities.blank import blank


class equipment:
    player = None
    compressed_inv = {}

    def __init__(self, player):
        equipment.player = player

    @staticmethod
    def equip_prompt():

        equipment.check_for_none()

        ans = gen_menu_num("What would you like to do?",
                           ["Switch Equipment or De-Equip", "Swap Abilities", "View your Current Inventory",
                            "View your Stats", "Leave"],
                           "What do you want to do?", 0)

        if ans == 1:
            equipment.equipment_handler()

        if ans == 2:
            equipment.equip_ability()

        if ans == 3:
            equipment.view_inv()

        if ans == 4:
            equipment.view_stats()

        if ans == 5:
            equipment.player.returning(0)

    @staticmethod
    def equipment_handler():
        player = equipment.player

        answer = gen_menu_num("Here are all of your equipped items:",
                              [item.name + " - " + item.desc + "\n" for item in player.equipped] +
                              ["Back"], "Do you want to switch/de-equip an item?", 0)

        if answer == 7:
            equipment.equip_prompt()

        else:

            while True:
                ans = gen_menu_num("What item would you like to switch: ",
                                   [item.name + " - " + item.desc + "\n" for item in
                                    player.inventory[player.equipped[answer - 1].type]] + ["De-Equip\n"],
                                   "Pick an item.", 0)

                # if de-equipping
                if ans == len(player.inventory[player.equipped[answer - 1].type]) + 1:

                    if player.equipped[answer - 1] in (fists, shoes, shirt, pants, no_helmet, no_accessory):
                        print(f"{colors.Red} You cannot de-equip this item. {colors.Reset}")

                    # adds equipped item to inventory if not any from above
                    else:
                        equipment.add_to_inv_secret(player.equipped[answer - 1])
                        player.equipped[answer - 1] = None
                        equipment.check_for_none()

                # if switching
                else:

                    inventory_item = player.inventory[player.equipped[answer - 1].type][ans - 1]
                    equipped = player.equipped[answer - 1]
                    #print(inventory_item)
                    # if the item is not a fist, or any blank item, then add it back to the inventory.
                    if equipped not in (fists, shoes, shirt, pants, no_helmet, no_accessory):
                        equipment.add_to_inv(equipped)

                    # item equipped becomes item that was in my inventory
                    player.equipped[answer - 1] = inventory_item
                    print(f"{colors.LightBlue}{inventory_item.name} has been equipped.{colors.Reset}\n")

                    # the item in my inventory is now deleted from my inventory
                    equipment.del_item(inventory_item)
                    #print(equipment.compressed_inv)

                equipment.equipment_handler()

    @staticmethod
    def equip_ability():

        equipment.player.abilities = equipment.player.abilities + [blank] * (4 - len(equipment.player.abilities))

        while True:
            ans = gen_menu_num("Pick an ability to switch: ", [ability.name + " - " + ability.desc + "\n" for ability in
                                                               equipment.player.abilities] + ["Back"],
                               "What would you like to do? ", 0)

            if ans == 5:
                equipment.equip_prompt()

            else:
                a = gen_menu_num("Choose an item to switch it with: ",
                                 [ability.name + " - " + ability.desc + "\n" for ability in
                                  equipment.player.ability_inv] + ["Back"], "What would you like to do? ", 0)

                if a == len(equipment.player.ability_inv) + 1:
                    equipment.equip_ability()

                else:

                    if equipment.player.abilities[ans - 1] != blank:
                        equipment.add_to_inv(equipment.player.abilities[ans - 1])

                    equipment.player.abilities[ans - 1] = equipment.player.ability_inv[a - 1]

                    equipment.del_item(equipment.player.ability_inv[a - 1])

                equipment.equip_ability()

    @staticmethod
    def view_inv():
        player = equipment.player
        equipment.compress_inventory()

        listing = []
        typings = {1: "weapon", 2: "ability", 3: "helmet", 4: "chestplate", 5: "leggings", 6: "boots", 7: "material",
                   8: "accessory"}

        a = gen_menu_num(
            f"Here is what you can see in your inventory:\n\nYou have: {colors.Green}${player.money}{colors.Reset}",
            [f"{colors.LightRed}Weapons{colors.Reset}", f"{colors.Magenta}Abilities{colors.Reset}",
             f"{colors.Yellow}Helmets{colors.Reset}", f"{colors.Yellow}Chestplates{colors.Reset}",
             f"{colors.Yellow}Leggings{colors.Reset}",
             f"{colors.Yellow}Boots{colors.Reset}", f"{colors.Green}Accessories{colors.Reset}",
             f"{colors.White}Materials{colors.Reset}", f"Back"],
            "What would you like to see?", 0)

        if a != 9:
            while True:

                total_index = 0

                print(f"\n{colors.Yellow}Here's what you have: {colors.Reset}\n")

                for key in equipment.compressed_inv:
                    print(key)
                    print(equipment.compressed_inv)
                    if key.type == typings[a]:
                        total_index += 1

                        listing.append(key)

                        print(
                            f"{total_index}. {colors.Yellow}{equipment.compressed_inv[key]}x{colors.Reset} {key.name}")

                print(f"{total_index + 1}. {colors.LightRed}Back{colors.Reset}")

                try:
                    ans = int(input(f"\n{colors.Yellow}What would you like to learn more about?{colors.Reset}\n"))

                    if ans not in range(1, total_index + 2):
                        raise ValueError

                    if ans != total_index + 1:
                        print(f"\n{listing[ans - 1].name}: {listing[ans - 1].desc}")

                    else:
                        equipment.view_inv()

                except ValueError:
                    print(f"\n{colors.Red}That's not an option.{colors.Reset}\n")

        else:
            equipment.equip_prompt()

    @staticmethod
    def view_stats():
        equipment.player.update_stats(equipment.player.level)

        print(f"\nHere are your stats:\n"
              f"{colors.Green}HP{colors.Reset}: {colors.LightGreen}{equipment.player.hp}{colors.Reset} / {colors.LightGreen}{equipment.player.maxhp}{colors.Reset} ({colors.Blue}{equipment.player.raw_maxhp}{colors.Reset} + {colors.Magenta}{equipment.player.maxhp - equipment.player.raw_maxhp}{colors.Reset})\n"
              f"{colors.Red}DMG{colors.Reset}: {colors.LightRed}{equipment.player.dmg}{colors.Reset} ({colors.Blue}{equipment.player.raw_dmg}{colors.Reset} + {colors.Magenta}{equipment.player.dmg - equipment.player.raw_dmg}{colors.Reset})\n"
              f"{colors.Blue}CRT%{colors.Reset}: {colors.LightBlue}{equipment.player.crc}{colors.Reset} ({colors.Blue}{equipment.player.raw_crc}{colors.Reset} + {colors.Magenta}{equipment.player.crc - equipment.player.raw_crc}{colors.Reset})\n"
              f"{colors.Yellow}ARMOR{colors.Reset}: {colors.LightYellow}{equipment.player.armor}{colors.Reset} ({colors.Blue}{equipment.player.raw_armor}{colors.Reset} + {colors.Magenta}{equipment.player.armor - equipment.player.raw_armor}{colors.Reset})\n"
              f"{colors.Yellow}ARMOR%{colors.Reset}: {colors.LightYellow}{equipment.player.armor_percent * 100}%{colors.Reset} ({colors.Blue}{equipment.player.raw_armor_percent}{colors.Reset} + {colors.Magenta}{equipment.player.armor_percent - equipment.player.armor - equipment.player.raw_armor}{colors.Reset})\n"
              f"{colors.White}SPD{colors.Reset}: {equipment.player.speed} ({colors.Blue}{equipment.player.raw_speed}{colors.Reset} + {colors.Magenta}{equipment.player.speed - equipment.player.raw_speed}{colors.Reset})\n"
              f"{colors.LightRed}FIRE IMMUNE{colors.Reset}: {colors.Red}{equipment.player.immune_to_burn}{colors.Reset}\n"
              f"You have: {colors.Green}${equipment.player.money}{colors.Reset}\n")

        sleep(2)
        equipment.equip_prompt()

    ###################
    # UTILITY METHODS #
    ###################

    @staticmethod
    def force_equip(item):
        equipment.check_for_none()
        equipment.player.abilities = equipment.player.abilities + [blank] * (4 - len(equipment.player.abilities))

        # check for discovery

        if not item.discovered:
            equipment.player.lexicon.update_discovery(item)

        # prioritize replacing blanks
        # if there are no blanks, replace the first ability
        if item.type == "ability":

            for index in range(0, len(equipment.player.abilities)):

                # finds a blank first. If it does, equips it
                if equipment.player.abilities[index] == blank:
                    equipment.player.abilities[index] = item
                    break

                # if we made it to the end of the list and we haven't found a blank, we replace the first slot
                if index == 4:
                    equipment.add_to_inv_secret(equipment.player.abilities[0])
                    equipment.player.abilities[0] = item

        else:

            if item.type == "weapon":
                if equipment.player.weapon != fists:  # as long as item is not fists, we add to inv
                    equipment.add_to_inv_secret(equipment.player.weapon)
                equipment.player.equipped[
                    0] = item  # item is equipped, no need to delete anything since we are force equipping

            elif item.type == "helmet":
                if equipment.player.helmet != no_helmet:
                    equipment.add_to_inv_secret(equipment.player.helmet)
                equipment.player.equipped[1] = item

            elif item.type == "chestplate":
                if equipment.player.chestplate != shirt:
                    equipment.add_to_inv_secret(equipment.player.chestplate)
                equipment.player.equipped[2] = item

            elif item.type == "leggings":
                if equipment.player.leggings != pants:
                    equipment.add_to_inv_secret(equipment.player.leggings)
                equipment.player.equipped[3] = item

            elif item.type == "boots":
                if equipment.player.boots != shoes:
                    equipment.add_to_inv_secret(equipment.player.boots)
                equipment.player.equipped[4] = item

            elif item.type == "accessory":
                if equipment.player.accessory != no_accessory:
                    equipment.add_to_inv_secret(equipment.player.accessory)
                equipment.player.equipped[5] = item

        equipment.compress_inventory()
        equipment.check_for_none()

    @staticmethod
    def add_to_inv(item):

        print(f"\n{colors.Yellow}{item.name}{colors.Green} has been added to your inventory.{colors.Reset}\n")
        if item not in (fists, shoes, shirt, pants, no_helmet, no_accessory):
            if not item.discovered:
                equipment.player.lexicon.update_discovery(item)
            equipment.player.inventory[item.type].append(item)

        equipment.compress_inventory()

    @staticmethod
    def add_to_inv_secret(item):
        if item not in (fists, shoes, shirt, pants, no_helmet, no_accessory):
            if not item.discovered:
                equipment.player.lexicon.update_discovery(item)
            equipment.player.inventory[item.type].append(item)

        equipment.compress_inventory()

    @staticmethod
    def del_item(item):
        player = equipment.player
        #print(item.name)
        for i in range(0, len(player.inventory[item.type])):
            #print("I is iterating over: ", i, " which is item: ", player.inventory[item.type][i])
            if player.inventory[item.type][i] == item:
                del player.inventory[item.type][i]
                #print("after i delete: ", player.inventory[item.type])
                break
        equipment.compress_inventory()

    # a compressed inventory is an inventory that stores every single item in one dictionary. The item object is the key, and the amount of that object stored in your inventory is the number that follows.
    # this is used in shops, crafting, and anything that needs to quickly check your inventory for all required materials.
    @staticmethod
    def compress_inventory():

        comp_inv = equipment.player.inventory["weapon"] + equipment.player.inventory["helmet"] + \
                   equipment.player.inventory["chestplate"] + equipment.player.inventory["leggings"] + \
                   equipment.player.inventory["boots"] + equipment.player.inventory["material"] + \
                   equipment.player.inventory["accessory"] + equipment.player.inventory["ability"]
        equipment.compressed_inv = {}

        for item in comp_inv:
            if item not in equipment.compressed_inv:
                equipment.compressed_inv[item] = 1
            else:
                equipment.compressed_inv[item] += 1

            if equipment.compressed_inv[item] == 0:
                del equipment.compressed_inv[item]

    @staticmethod
    def check_for_none():
        player = equipment.player

        if player.equipped[0] == None:
            player.weapon = fists
        else:
            player.weapon = player.equipped[0]

        if player.equipped[1] == None:
            player.helmet = no_helmet
        else:
            player.helmet = player.equipped[1]

        if player.equipped[2] == None:
            player.chestplate = shirt
        else:
            player.chestplate = player.equipped[2]

        if player.equipped[3] == None:
            player.leggings = pants
        else:
            player.leggings = player.equipped[3]

        if player.equipped[4] == None:
            player.boots = shoes
        else:
            player.boots = player.equipped[4]

        if player.equipped[5] == None:
            player.accessory = no_accessory
        else:
            player.accessory = player.equipped[4]

        player.equipped = [player.weapon, player.helmet, player.chestplate, player.leggings, player.boots,
                           player.accessory]
