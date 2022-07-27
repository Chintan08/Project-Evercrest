from Core.menus import gen_menu_yn, gen_menu_num
from Utility.colors import colors
from time import sleep
from Utility.equipment import equipment

# TODO: redo this cringe
class shop:

    @staticmethod
    def shop(ans, shop_options, player):
        if not ans:
            ans = gen_menu_num(
                f"What would you like to do?\nYou have {colors.LightGreen}${player.money}{colors.Reset} currently.",
                [f"{colors.Green}Buy{colors.Reset}", f"{colors.Red}Sell{colors.Reset}",
                 f"{colors.Blue}Back{colors.Reset}"], "Pick an option: ", 0)

        # BUY
        if ans == 1:
            a = gen_menu_num(f"What type of item would you like to {colors.Green}buy{colors.Reset}?",
                             [f"{colors.LightRed}Weapons{colors.Reset}", f"{colors.Yellow}Helmets{colors.Reset}",
                              f"{colors.Yellow}Chestplates{colors.Reset}",
                              f"{colors.Yellow}Leggings{colors.Reset}",
                              f"{colors.Yellow}Boots{colors.Reset}",
                              f"{colors.LightGreen}Accessories{colors.Reset}", f"{colors.White}Materials{colors.Reset}",
                              f"{colors.Cyan}Back{colors.Reset}"],
                             "Pick an option: ", 0)

            while True:
                if a != 8:
                    total_index = 0
                    print(f"{colors.Cyan}Here's what we have for that:{colors.Reset} \n")

                    for index in range(0, len(shop_options[a])):
                        sleep(.1)
                        print(
                            f"{index + 1}. {shop_options[a][index].name}: {colors.LightGreen}${shop_options[a][index].buy}{colors.Reset}")
                        total_index = index + 1
                    print(f"{total_index + 1}. Back\n")

                else:
                    shop.shop(0, shop_options, player)

                try:
                    b = int(input(f"What would you like to {colors.Green}buy{colors.Reset}?\n"))

                    if b not in range(1, len(shop_options[a]) + 2):
                        raise ValueError

                    if b != total_index + 1:
                        c = int(
                            input(f"\nHow many would you like to {colors.Green}buy{colors.Reset}? (Input number)\n"))
                        d = gen_menu_yn(
                            f"Are you sure you want to {colors.Green}buy{colors.Reset} {colors.Yellow}{c}x{colors.Reset} {shop_options[a][b - 1].name}?")

                        if d:

                            if (shop_options[a][b - 1].buy * c) > player.money:
                                print(f"{colors.Red}You don't have enough money!{colors.Reset}\n")
                                shop.shop(1, shop_options, player)

                            else:
                                if shop_options[a][b - 1].type == "helmet" or shop_options[a][
                                    b - 1].type == "chestplate" or shop_options[a][b - 1].type == "leggings" or \
                                        shop_options[a][b - 1].type == "boots":

                                    for index in range(0, c):
                                        equipment.add_to_inv(shop_options[a][b - 1])
                                        player.money -= shop_options[a][b-1].buy

                                    shop.shop(1, shop_options, player)

                                else:
                                    for index in range(0, c):
                                        equipment.add_to_inv(shop_options[a][b - 1])
                                        player.money -= shop_options[a][b - 1].buy
                                    shop.shop(1, shop_options, player)

                                print(
                                    f"You bought {shop_options[a][b - 1].name} for {shop_options[a][b - 1].buy}! You now have {colors.LightGreen}{player.money}{colors.Reset}.")

                    else:
                        shop.shop(1, shop_options, player)

                except ValueError:
                    print("That's not an option.")

        # SELL
        elif ans == 2:

            a = gen_menu_num(f"What type of item would you like to {colors.Red}sell{colors.Reset}?",
                             [f"{colors.LightRed}Weapons{colors.Reset}", f"{colors.Yellow}Helmets{colors.Reset}",
                              f"{colors.Yellow}Chestplates{colors.Reset}",
                              f"{colors.Yellow}Leggings{colors.Reset}",
                              f"{colors.Yellow}Boots{colors.Reset}",
                              f"{colors.LightGreen}Accessories{colors.Reset}", f"{colors.White}Materials{colors.Reset}",
                              f"{colors.Cyan}Back{colors.Reset}"],
                             "Pick an option: ", 0)

            item_list = {1: player.inventory["weapon"], 2: player.inventory["helmet"], 3: player.inventory["chestplate"],
                         4: player.inventory["leggings"], 5: player.inventory["boots"], 6: player.inventory["accessory"],
                         7: player.inventory["material"]}

            while True:
                if a != 8:
                    total_index = 0
                    print(f"Here's what you have: \n")

                    if len(item_list[a]) < 1:
                        print(f"{colors.Red}You have nothing.{colors.Reset}\n")
                        shop.shop(2, shop_options, player)

                    for index in range(0, len(item_list[a])):
                        if item_list[a][index].sell is None:
                            print(f"{index + 1}. {item_list[a][index].name}: Unsellable!")
                        else:
                            print(f"{index + 1}. {item_list[a][index].name}: ${item_list[a][index].sell}")
                        total_index = index + 1
                    print(f"{total_index + 1}. Back\n")

                    try:
                        b = int(input(f"What would you like to {colors.Red}sell{colors.Reset}? (Input number)"))

                        if b not in range(1, len(item_list[a]) + 2):
                            raise ValueError

                        if b == total_index + 1:
                            shop.shop(2, shop_options, player)

                        if item_list[a][b - 1].sell is None:
                            print(f"\n{colors.Red}This item is priceless! It cannot be sold.{colors.Reset}\n")
                            shop.shop(2, shop_options, player)

                        d = gen_menu_yn(
                            f'Are you sure you want to {colors.Red}sell{colors.Reset} {item_list[a][b - 1].name}?')

                        if d:

                            if b != total_index + 1:
                                player.money += item_list[a][b - 1].sell
                                print(f"You sold {item_list[a][b - 1].name} for ${item_list[a][b - 1].sell}!")
                                print(f"You now have ${player.money}.")

                                equipment.del_item(item_list[a][b-1])
                                shop.shop(2, shop_options, player)

                            else:
                                shop.shop(2, shop_options, player)
                        else:
                            shop.shop(2, shop_options, player)

                    except ValueError:
                        print("That's not an option.")

                else:
                    shop.shop(0, shop_options, player)

        else:
            player.returning(0)
