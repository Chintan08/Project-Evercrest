from Items.Armor.Boots.golagtatite_shoes import golagtatite_shoes
from Items.Armor.Chestplates.golagplate import golagplate
from Items.Armor.Helmets.mountain_helmet import mountain_helmet
from Items.Armor.Leggings.wolf_pants import wolf_pants
from Items.Weapons.golagtatite_sword import golagtatite_sword
from Utility.equipment import *

class craft:

    @staticmethod
    def crafting(player):

        equipment.compress_inventory()

        confirmed = 0
        can_craft = False

        ans = gen_menu_num(f"{colors.Yellow}Here's what you can craft{colors.Reset}: ",
                           [f"{colors.LightRed}Weapons{colors.Reset}",
                            f"{colors.Yellow}Helmets{colors.Reset}",
                            f"{colors.Yellow}Chestplates{colors.Reset}",
                            f"{colors.Yellow}Leggings{colors.Reset}",
                            f"{colors.Yellow}Boots{colors.Reset}",
                            f"{colors.LightGreen}Accessories{colors.Reset}",
                            f"{colors.Cyan}Back{colors.Reset}"],
                           f"{colors.Cyan}What would you like to do?{colors.Reset}", 0)

        craftable_weapons = [golagtatite_sword]
        craftable_helmets = [mountain_helmet]
        craftable_chestplates = [golagplate]
        craftable_leggings = [wolf_pants]
        craftable_boots = [golagtatite_shoes]
        craftable_accessories = []

        craftable = [craftable_weapons, craftable_helmets, craftable_chestplates, craftable_leggings, craftable_boots, craftable_accessories]

        if ans != 7:

            while True:
                try:

                    total_index = 0
                    print(f"{colors.Yellow}Here's what you can craft{colors.Reset}: \n")

                    for index in range(0, len(craftable[ans - 1])):

                        discovery_total = 0
                        recipe_amount = 0
                        for item in craftable[ans - 1][index].recipe:
                            recipe_amount += 1
                            if item in player.lexion.lexicon_dict[item.type]:
                                discovery_total += 1

                        if not craftable[ans - 1][index].lvl_req > player.level and recipe_amount == discovery_total:
                            print(f"{index + 1}. {craftable[ans - 1][index].name}\n{craftable[ans - 1][index].print_recipe()}\n")

                            total_index += 1

                    print(f"{total_index + 1}. Back\n")

                    a = int(input(f"{colors.Blue}What would you like to craft?{colors.Reset}\n"))

                    if a not in range(0, len(craftable[ans - 1]) + 2):
                        raise ValueError

                    if a == total_index + 1:
                        craft.crafting(player)

                    else:

                        print("\n" + craftable[ans-1][a-1].desc + "\n")
                        sleep(.5)
                        yn_ans = gen_menu_yn("Are you sure you want to craft this item?")

                        if yn_ans:

                            for req in craftable[ans - 1][a - 1].recipe:

                                try:

                                    if equipment.compressed_inv[req] >= craftable[ans - 1][a - 1].recipe[req]:
                                        confirmed += 1

                                    elif equipment.compressed_inv[req] < craftable[ans - 1][a - 1].recipe[req]:
                                        print(f"\n{colors.Red}You don't have enough materials!{colors.Reset}\n")
                                        break

                                    if confirmed == len(craftable[ans - 1][a - 1].recipe):
                                        can_craft = True
                                        break

                                except KeyError:
                                    print(f"\n{colors.Red}You don't have a certain material!{colors.Reset}\n")
                                    break

                            if can_craft:
                                index = 0
                                current_item = []

                                for item in craftable[ans - 1][a - 1].recipe:
                                    current_item = current_item + ([item] * craftable[ans - 1][a - 1].recipe[item])

                                while index != len(current_item):

                                    for item in range(0, len(player.inventory[current_item[index].type])):

                                        if player.inventory[current_item[index].type][item].name == current_item[index].name:
                                            del player.inventory[current_item[index].type][item]

                                            equipment.compress_inventory()

                                            break

                                    index += 1

                                equipment.add_to_inv(craftable[ans - 1][a - 1])
                                craft.crafting(player)

                        else:
                            craft.crafting(player)

                except ValueError:
                    print(f"That's not an option.")

        else:
            player.returning(0)
