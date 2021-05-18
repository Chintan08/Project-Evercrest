from Items.Weapons.wooden_sword import wooden_sword
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

        craftable_weapons = [wooden_sword]
        craftable_helmets = []
        craftable_chestplates = []
        craftable_leggings = []
        craftable_boots = []
        craftable_accessories = []
        craftable_potions = []

        craftable = [craftable_weapons, craftable_helmets, craftable_chestplates, craftable_leggings, craftable_boots, craftable_accessories, craftable_potions]

        if ans != 7:

            while True:
                try:

                    total_index = 0
                    print(f"{colors.Yellow}Here's what you can craft{colors.Reset}: \n")

                    for index in range(0, len(craftable[ans - 1])):

                        if not craftable[ans - 1][index].lvl_req > player.level:
                            print(
                                f"{index + 1}. {craftable[ans - 1][index].name}\n{craftable[ans - 1][index].print_recipe()}\n")

                            total_index += 1

                    print(f"{total_index + 1}. Back\n")

                    a = int(input(f"{colors.Blue}What would you like to craft?{colors.Reset}\n"))

                    if a not in range(0, len(craftable[ans - 1]) + 2):
                        raise ValueError

                    if a == total_index + 1:
                        craft.crafting(player)

                    else:

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

                                for item in range(0, len(player.inv[current_item[index].type])):

                                    if player.inv[current_item[index].type][item].name == current_item[index].name:
                                        del player.inv[current_item[index].type][item]

                                        player.compressed_inv[current_item[index]] -= 1

                                        break

                                index += 1

                            player.add_to_inv(craftable[ans - 1][a - 1].type, craftable[ans - 1][a - 1])
                            craft.crafting(player)

                except ValueError:
                    print(f"That's not an option.")

        else:
            player.returning(0)