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

        print(
            f"{colors.LightRed}\n\n\n\n"
            f" _____ _                ___                                  \n"
            f"|_   _| |              / _ \                                 \n"
            f"  | | | |__   ___     / /_\ \_ __ _ __ ___   ___  _ __ _   _ \n"
            f"  | | | '_ \ / _ \    |  _  | '__| '_ ` _ \ / _ \| '__| | | |\n"
            f"  | | | | | |  __/    | | | | |  | | | | | | (_) | |  | |_| |\n"
            f"  \_/ |_| |_|\___|    \_| |_/_|  |_| |_| |_|\___/|_|   \__, |\n"
            f"                                                        __/ |\n"
            f"                                                       |___/ \n"
            f"{colors.Reset}"
        )

        print(f"\n{colors.LightYellow}Here's what you have equipped right now: {colors.Reset}\n\n"
              f"Weapon: {equipment.player.equipped[0].name}\n"
              f"Helmet: {equipment.player.equipped[1].name}\n"
              f"Chestplate: {equipment.player.equipped[2].name}\n"
              f"Leggings: {equipment.player.equipped[3].name}\n"
              f"Boots: {equipment.player.equipped[4].name}\n"
              f"Accessory: {equipment.player.equipped[5].name}\n"
              f"Abilities: {equipment.player.abilities[0].name}, {equipment.player.abilities[1].name}, {equipment.player.abilities[2].name}, {equipment.player.abilities[3].name}")

        ans = gen_menu_num("What would you like to do?",
                           [f"{colors.LightYellow}Switch Equipment or De-Equip{colors.Reset}", f"{colors.LightMagenta}Swap Abilities{colors.Reset}", f"{colors.LightGreen}View your Current Inventory{colors.Reset}",
                            f"{colors.LightCyan}View your Stats{colors.Reset}", f"{colors.LightRed}Leave{colors.Reset}"],
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
                                    player.inventory[player.equipped[answer - 1].type]] + ["De-Equip\n"] + ["Back\n"],
                                   "Pick an item.", 0)

                # if back
                if ans == len(player.inventory[player.equipped[answer - 1].type]) + 2:
                    equipment.equipment_handler()

                # if de-equipping
                if ans == len(player.inventory[player.equipped[answer - 1].type]) + 1:

                    equipment.deequip_item(player.equipped[answer - 1], False)

                # if switching
                else:

                    inventory_item = player.inventory[player.equipped[answer - 1].type][ans - 1]

                    # check for level requirement
                    if player.level < inventory_item.lvl_req:
                        print(
                            f"\n{colors.LightRed}You are too low of a level to equip this item. The item needs you to be level {inventory_item.lvl_req} to equip it.{colors.Reset}")
                        equipment.equipment_handler()

                    equipped = player.equipped[answer - 1]

                    # if the item is not a fist, or any blank item, then add it back to the inventory.
                    if equipped not in (fists, shoes, shirt, pants, no_helmet, no_accessory):
                        equipment.add_to_inv(equipped)

                    # item equipped becomes item that was in my inventory
                    player.equipped[answer - 1] = inventory_item
                    print(f"{colors.LightBlue}{inventory_item.name} has been equipped.{colors.Reset}\n")

                    # the item in my inventory is now deleted from my inventory
                    equipment.del_item(inventory_item)

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
                                  equipment.player.inventory["ability"]] + ["Back"], "What would you like to do? ", 0)

                if a == len(equipment.player.inventory["ability"]) + 1:
                    equipment.equip_ability()

                else:

                    if equipment.player.abilities[ans - 1] != blank:
                        equipment.add_to_inv(equipment.player.abilities[ans - 1])

                    equipment.player.abilities[ans - 1] = equipment.player.inventory["ability"][a - 1]

                    equipment.del_item(equipment.player.inventory["ability"][a - 1])

                equipment.equip_ability()

    @staticmethod
    def view_inv():
        player = equipment.player
        equipment.compress_inventory()

        listing = []
        typings = {1: "weapon", 2: "ability", 3: "helmet", 4: "chestplate", 5: "leggings", 6: "boots", 7: "accessory",
                   8: "material"}

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

                    if key.type == typings[a]:
                        total_index += 1

                        listing.append(key)

                        print(f"{total_index}. {colors.Yellow}{equipment.compressed_inv[key]}x{colors.Reset} {key.name}")

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
              f"{colors.Green}HP: {colors.LightGreen}{equipment.player.hp}{colors.Reset} / {colors.LightGreen}{equipment.player.maxhp}{colors.Reset} ({colors.Blue}{equipment.player.raw_maxhp}{colors.Reset} + {colors.Magenta}{equipment.player.maxhp - equipment.player.raw_maxhp}{colors.Reset})\n"
              f"{colors.Red}DMG: {colors.LightRed}{equipment.player.dmg}{colors.Reset} ({colors.Blue}{equipment.player.raw_dmg}{colors.Reset} + {colors.Magenta}{equipment.player.dmg - equipment.player.raw_dmg}{colors.Reset})\n"
              f"{colors.Blue}CRT%: {colors.LightBlue}{equipment.player.crc}{colors.Reset} ({colors.Blue}{equipment.player.raw_crc}{colors.Reset} + {colors.Magenta}{equipment.player.crc - equipment.player.raw_crc}{colors.Reset})\n"
              f"{colors.Yellow}ARMOR: {colors.LightYellow}{equipment.player.armor}{colors.Reset} ({colors.Blue}{equipment.player.raw_armor}{colors.Reset} + {colors.Magenta}{equipment.player.armor - equipment.player.raw_armor}{colors.Reset})\n"
              f"{colors.Yellow}ARMOR%: {colors.LightYellow}{equipment.player.armor_percent * 100}%{colors.Reset} ({colors.Blue}{equipment.player.raw_armor_percent}{colors.Reset} + {colors.Magenta}{equipment.player.armor_percent - equipment.player.raw_armor_percent}{colors.Reset})\n"
              f"{colors.White}SPD: {equipment.player.speed} ({colors.Blue}{equipment.player.raw_speed}{colors.Reset} + {colors.Magenta}{equipment.player.speed - equipment.player.raw_speed}{colors.Reset})\n"
              f"{colors.LightRed}FIRE RESIST: {colors.Red}{equipment.player.fire_resistance * 100}%\n"
              f"{colors.Yellow}SHOCK RESIST: {colors.LightYellow}{equipment.player.shock_resistance * 100}%{colors.Reset}\n"
              f"You have: {colors.Green}${equipment.player.money}{colors.Reset}\n"
              f"\n{colors.Red}COMBAT LEVELS{colors.Reset}\n"
              f"{colors.Magenta}XP BONUS: {colors.LightMagenta}{equipment.player.xp_bonus}{colors.Reset} ({colors.Blue}{equipment.player.raw_xp_bonus}{colors.Reset} + {colors.Magenta}{equipment.player.xp_bonus - equipment.player.raw_xp_bonus}{colors.Reset})\n"
              f"{colors.Cyan}Total Combat Level: {colors.LightCyan}{equipment.player.total_combat_level}{colors.Reset}\n"
              f"{colors.Yellow}Standard Level: {colors.LightYellow}{equipment.player.combat_level['standard']} ({equipment.player.combat_xp['standard']} / {equipment.player.combat_req['standard']} XP)\n"
              f"{colors.Yellow}Brawling Level: {colors.LightYellow}{equipment.player.combat_level['brawler']} ({equipment.player.combat_xp['brawler']} / {equipment.player.combat_req['brawler']} XP)\n"
              f"{colors.Yellow}Dueling Level: {colors.LightYellow}{equipment.player.combat_level['dueling']} ({equipment.player.combat_xp['dueling']} / {equipment.player.combat_req['dueling']} XP)\n"
              f"{colors.Yellow}Elitist Level: {colors.LightYellow}{equipment.player.combat_level['elitist']} ({equipment.player.combat_xp['elitist']} / {equipment.player.combat_req['elitist']} XP)\n"
              f"{colors.Yellow}Nimbilic Level: {colors.LightYellow}{equipment.player.combat_level['nimbilic']} ({equipment.player.combat_xp['nimbilic']} / {equipment.player.combat_req['nimbilic']} XP)\n"
              f"{colors.Yellow}Resolute Level: {colors.LightYellow}{equipment.player.combat_level['resolute']} ({equipment.player.combat_xp['resolute']} / {equipment.player.combat_req['resolute']} XP)\n"
              f"{colors.Yellow}Eldric Level: {colors.LightYellow}{equipment.player.combat_level['eldric']} ({equipment.player.combat_xp['eldric']} / {equipment.player.combat_req['eldric']} XP)\n"
              f"\n{colors.Magenta}RACE INFORMATION{colors.Reset}\n"
              f"{colors.Blue}Race: {colors.Reset}{equipment.player.race.name}\n"
              f"{colors.Green}HP: {colors.LightGreen}{equipment.player.race.hp}{colors.Reset} HP {colors.LightGreen}(+{equipment.player.race.hp_scale} per level up)\n"
              f"{colors.Red}DMG: {colors.LightRed}{equipment.player.race.dmg}{colors.Reset} DMG {colors.LightRed}(+{equipment.player.race.dmg_scale} per level up)\n"
              f"{colors.Blue}CRT%: {colors.LightBlue}{equipment.player.race.crc}{colors.Reset} CRC% {colors.LightBlue}(+{equipment.player.race.crc_scale} per level up)\n"
              f"{colors.Yellow}ARMOR: {colors.LightYellow}{equipment.player.race.armor}{colors.Reset} ARMOR {colors.LightYellow}(+{equipment.player.race.armor_scale} per level up)\n"
              f"{colors.Yellow}ARMOR%: {colors.LightYellow}{equipment.player.race.armor_percent}{colors.Reset} ARMOR% {colors.LightYellow}(+{equipment.player.race.armor_percent_scale} per level up)\n"
              f"{colors.White}SPD: {equipment.player.race.speed} SPD (+{equipment.player.race.spd_scale} per level up)\n"
              f"{colors.Magenta}XP BONUS: {colors.LightMagenta}{equipment.player.race.xp_bonus} XP (+{equipment.player.race.xp_scale} per level up)\n"
              f"{colors.LightRed}FIRE RESIST: {colors.Red}{equipment.player.race.fire_resistance * 100}% DAMAGE RESISTED\n"
              f"{colors.Yellow}SHOCK RESIST: {colors.LightYellow}{equipment.player.race.shock_resistance * 100}% DAMAGE RESISTED{colors.Reset}")

        sleep(2)
        equipment.equip_prompt()

    ###################
    # UTILITY METHODS #
    ###################

    # Force Equipping is when the game puts an item in a player's item slot and puts the item they had in their inventory.
    @staticmethod
    def force_equip(item):
        equipment.check_for_none()
        equipment.player.abilities = equipment.player.abilities + [blank] * (4 - len(equipment.player.abilities))

        # check for discovery

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
            equipment.player.lexicon.update_discovery(item)
            equipment.player.inventory[item.type].append(item)

        equipment.compress_inventory()

    @staticmethod
    def add_to_inv_secret(item):
        if item not in (fists, shoes, shirt, pants, no_helmet, no_accessory):
            equipment.player.lexicon.update_discovery(item)
            equipment.player.inventory[item.type].append(item)

        equipment.compress_inventory()

    @staticmethod
    def deequip_item(item, is_secret):

        list_index = 0
        for index in range(0, len(equipment.player.equipped)):
            if item.type == equipment.player.equipped[index].type:
                list_index = index
                break

        if equipment.player.equipped[list_index] in (fists, shoes, shirt, pants, no_helmet, no_accessory):
            if not is_secret:
                print(f"{colors.Red}You cannot de-equip this item.{colors.Reset}")

        # adds equipped item to inventory if not any from above
        else:
            equipment.add_to_inv_secret(equipment.player.equipped[list_index])
            equipment.player.equipped[list_index] = None
            equipment.check_for_none()

    @staticmethod
    def del_item(item):
        player = equipment.player
        for i in range(0, len(player.inventory[item.type])):
            if player.inventory[item.type][i] == item:
                del player.inventory[item.type][i]
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

        if player.equipped[0] is None:
            player.weapon = fists
        else:
            player.weapon = player.equipped[0]

        if player.equipped[1] is None:
            player.helmet = no_helmet
        else:
            player.helmet = player.equipped[1]

        if player.equipped[2] is None:
            player.chestplate = shirt
        else:
            player.chestplate = player.equipped[2]

        if player.equipped[3] is None:
            player.leggings = pants
        else:
            player.leggings = player.equipped[3]

        if player.equipped[4] is None:
            player.boots = shoes
        else:
            player.boots = player.equipped[4]

        if player.equipped[5] is None:
            player.accessory = no_accessory
        else:
            player.accessory = player.equipped[5]

        player.equipped = [player.weapon, player.helmet, player.chestplate, player.leggings, player.boots,
                           player.accessory]
