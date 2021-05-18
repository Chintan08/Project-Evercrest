from Races.human import human
from Races.grayed import grayed
from Core.player import player
from Core.menus import gen_menu_num, gen_menu_yn
from Utility.colors import colors


class char_create:

    # list of all races, used in char create to choose race
    race_list = [human, grayed]

    # main method that will handle creating character
    @staticmethod
    def char_create():

        # name selector, asks for a string input then returns 1 or 0 if that is the desired name. While loop breaks
        # and moves on after name is received
        while True:
            player_name = f"{colors.LightGreen}{input(f'{colors.LightCyan}What is your name?{colors.Reset} ')}{colors.Reset}"
            print("\n")
            answer = gen_menu_yn(f"Are you sure your name is {player_name}?")
            if answer == 1:
                break
            else:
                pass

        # gets race selection here by printing out descriptor
        answer = gen_menu_num("Pick your race: ", [race.descriptor for race in char_create.race_list], "What would you like to choose?", 0)

        # return back to main, while also initializing this object Player.
        return player(player_name, char_create.race_list[answer - 1])