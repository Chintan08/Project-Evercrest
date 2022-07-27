from Core.menus import gen_menu_num
from time import sleep
from colored import fore, style
from Utility.colors import colors

# The Lexicon is the biggest core piece of this project. It will take all new entries and give discovery points based off of that.
# This will manage discovery points, quest logs, and more
from Utility.dialogue import dialogue


class lexicon(object):

    disc_points = 0
    lvl_req = 5

    # discovered arrays
    quests = []
    materials = []
    weapons = []
    accessories = []
    armor = []
    abilities = []
    enemies = []
    characters = []
    locations = []
    styles = []

    lexicon_dict = {"quest": quests, "material": materials, "weapon": weapons, "accessory": accessories, "armor": armor, "ability": abilities, "enemy": enemies, "character": characters, "location": locations, "style": styles}

    def __init__(self, player):
        self.player = player

    # updates points and will level up if needed
    def update_discovery(self, discovered):

        type = discovered.type
        if type in ("helmet", "chestplate", "leggings", "boots"):
            type = "armor"

        if discovered not in self.lexicon_dict[type]:

            if type in ("location", "enemy"):
                dialogue.dia(None, discovered.undiscovered_desc)

            self.disc_points += 1

            self.lexicon_dict[type].append(discovered)
            print(f"\n{fore.CYAN_2}You logged{style.RESET} {fore.GOLD_3B}{discovered.name}{style.RESET} {fore.CYAN_2}into your lexicon.{style.RESET}")

            print(f"You are now at {fore.DARK_GOLDENROD}{self.disc_points}{style.RESET} / {fore.DARK_GOLDENROD}{self.lvl_req}{style.RESET} {fore.BLUE}Discovery Points.{style.RESET}\n")
            sleep(1)

            if self.disc_points == self.lvl_req:
                dialogue.dia(None, f"\n{colors.Green}You leveled up!{colors.Reset} You are now at Level {colors.Yellow}{self.player.level + 1}{colors.Reset}! You increased some stats.")
                self.player.update_stats(self.player.level + 1)
                self.disc_points = 0
                self.lvl_req += int(self.lvl_req*.3)

    def view_prompt(self):
        lexicon_num = {1: self.lexicon_dict["quest"], 2: self.lexicon_dict["material"], 3: self.lexicon_dict["weapon"], 4: self.lexicon_dict["accessory"], 5: self.lexicon_dict["armor"], 6: self.lexicon_dict["ability"], 7: self.lexicon_dict["enemy"],
                       8: self.lexicon_dict["character"], 9: self.lexicon_dict["location"], 10: self.lexicon_dict["style"]}

        print(f"\nYou are at {colors.LightYellow}{self.disc_points}{colors.Reset} / {colors.Yellow}{self.lvl_req}{colors.Reset} points. You are {colors.Blue}Level {colors.Yellow}{self.player.level}{colors.Reset}.")
        a = gen_menu_num("What discovered items would you like to see?", [f"{colors.LightMagenta}Quests{colors.Reset}", f"{colors.White}Materials{colors.Reset}", f"{colors.Red}Weapons{colors.Reset}", f"{colors.Green}Accessories{colors.Reset}", f"{colors.Yellow}Armor{colors.Reset}", f"{colors.Magenta}Abilities{colors.Reset}", f"{colors.LightRed}Enemies{colors.Reset}", f"{colors.LightCyan}Characters{colors.Reset}", f"{colors.LightYellow}Locations{colors.Reset}", f"{colors.Magenta}Styles{colors.Reset}", f"{colors.Red}Enemies Killed{colors.Reset}", f"Back"], "What would you like to see? ", 0)

        # view kills
        if a == 11:
            print(f"\nHere are the enemies you have killed:\n")
            kill_list = self.compress_kills()
            for index in kill_list:
                print(f"{colors.Red}{index}: {colors.LightRed}{kill_list[index]} Killed {colors.Reset}\n")

            sleep(2)
            self.view_prompt()

        # back
        elif a == 12:
            self.player.returning(0)

        else:

            while True:
                answer = gen_menu_num("Here's what you have discovered: ", [lex.name for lex in lexicon_num[a]] + ["Back"], "What would you like to do?", 0)
                if answer == len(lexicon_num[a])+1:
                    self.view_prompt()
                else:
                    print(f"\n{lexicon_num[a][answer - 1].name}: {lexicon_num[a][answer-1].desc}")

    def is_discovered(self, discovery):

        if discovery in self.lexicon_dict[discovery.type]:
            return 1

        else:
            return 0

    def compress_kills(self):

        kill_list = self.player.enemies_killed
        kill_dict = {}

        for enemy in kill_list:
            if enemy not in kill_dict:
                kill_dict[enemy] = 1
            else:
                kill_dict[enemy] += 1

        return kill_dict
