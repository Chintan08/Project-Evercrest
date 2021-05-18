from Core.menus import gen_menu_num
from time import sleep
from colored import fore, style
from Utility.colors import colors

# The Lexicon is the biggest core piece of this project. It will take all new entries and give discovery points based off of that.
# This will manage discovery points, quest logs, and more


class lexicon:

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
    lexicon_num = {1: quests, 2: materials, 3: weapons, 4: accessories, 5: armor, 6: abilities, 7: enemies, 8: characters, 9: locations, 10: styles}

    def __init__(self, player):
        self.player = player

    # updates points and will level up if needed
    def update_discovery(self, discovered):
        self.disc_points += 1
        type = discovered.type
        discovered.discovered = True

        self.lexicon_dict[type].append(discovered)
        print(f"\n{fore.CYAN_2}You logged{style.RESET} {fore.GOLD_3B}{discovered.name}{style.RESET} {fore.CYAN_2}into your lexicon.{style.RESET}")

        print(f"You are now at {fore.DARK_GOLDENROD}{self.disc_points}{style.RESET} / {fore.DARK_GOLDENROD}{self.lvl_req}{style.RESET} {fore.BLUE}Discovery Points.{style.RESET}\n")
        sleep(1)
        if self.disc_points == self.lvl_req:
            print(f"{colors.Green}You leveled up!{colors.Reset} You are now at Level {colors.Yellow}{self.player.level + 1}{colors.Reset}! You increased some stats.\n")
            self.player.update_stats(self.player.level + 1)
            self.disc_points = 0
            self.lvl_req += int(self.lvl_req*.7)

    def view_prompt(self):
        print(f"\nYou are at {colors.LightYellow}{self.disc_points}{colors.Reset} / {colors.Yellow}{self.lvl_req}{colors.Reset} points. You are {colors.Blue}Level {colors.Yellow}{self.player.level}{colors.Reset}.")
        a = gen_menu_num("What discovered items would you like to see?", [f"{colors.LightMagenta}Quests{colors.Reset}", f"{colors.White}Materials{colors.Reset}", f"{colors.Red}Weapons{colors.Reset}", f"{colors.Green}Accessories{colors.Reset}", f"{colors.Yellow}Armor{colors.Reset}", f"{colors.Magenta}Abilities{colors.Reset}", f"{colors.LightRed}Enemies{colors.Reset}", f"{colors.LightCyan}Characters{colors.Reset}", f"{colors.LightYellow}Locations{colors.Reset}", f"{colors.Magenta}Styles{colors.Reset}", f"{colors.Red}Enemies Killed{colors.Reset}", f"Back"], "What would you like to see? ", 0)

        # view kills
        if a == 11:
            print(f"\nHere are the enemies you have killed:\n")

            for index in self.player.enemies_killed:
                print(f"{colors.Red}{index}: {colors.LightRed}{self.player.enemies_killed[index]} Killed {colors.Reset}\n")

            self.view_prompt()

        # back
        elif a == 12:
            self.player.returning(0)

        else:

            while True:
                answer = gen_menu_num("Here's what you have discovered: ", [lex.name for lex in self.lexicon_num[a]] + ["Back"], "What would you like to do?", 0)
                if answer == len(self.lexicon_num[a])+1:
                    self.view_prompt()
                else:
                    print(f"\n{self.lexicon_num[a][answer - 1].name}: {self.lexicon_num[a][answer-1].desc}")

