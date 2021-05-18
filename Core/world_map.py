from Core.menus import *
from Kingdoms.Stronia.stronia import stronia


class world_map:

    @staticmethod
    def world_options(player):

        # creates a return point so you can return back to the world map when you call on that specific method
        player.return_to_world(world_map)

        ans = gen_menu_num("Where would you like to go?", [f"{colors.LightYellow}Stronia{colors.Reset}",
                                                           f"{colors.LightYellow}Valatene{colors.Reset}",
                                                           f"{colors.LightYellow}Drummond{colors.Reset}",
                                                           f"{colors.LightYellow}Jargus{colors.Reset}",
                                                           f"{colors.LightYellow}Zanio{colors.Reset}",
                                                           f"{colors.LightYellow}Faronwood{colors.Reset}",
                                                           f"{colors.LightYellow}Cyliac{colors.Reset}",
                                                           f"{colors.LightYellow}Rendagger{colors.Reset}",
                                                           f"{colors.LightYellow}Shellamond{colors.Reset}",
                                                           f"{colors.LightYellow}Krion{colors.Reset}",
                                                           f"{colors.Red}Quit Game{colors.Red}"],
                           "Pick an option to learn more, and to go there: ", .075)

        # a list of all kingdoms
        # TODO: import all kingdoms, and then add them to the list
        kingdoms = {1: stronia}

        # if answer is quit game, quits game
        if ans == 11:
            quit()

        # if you didn't quit the game, takes the number from the previous generated menu and calls on the kingdom you
        # picked.
        selected_kingdom = kingdoms[ans](player)

        # Asks if you'd like to go to the chosen kingdom. If you do, you get taken to their menu prompt.
        # TODO: Add Quest Reminders in each Kingdom once Quests are implemented
        a = gen_menu_yn(f"{selected_kingdom.desc} \n{colors.LightCyan}Would you like to go there?{colors.Reset}")
        if a:
            selected_kingdom.menu_prompt()
        else:
            world_map.world_options(player)
