import ctypes
import os
from time import sleep

from Core.character_creator import char_create
from Core.lexicon import lexicon
from Core.menus import gen_menu_yn, gen_menu_num
from Core.world_map import world_map
from Items.Abilities.Resolute.body_bash import body_bash
from Items.Abilities.Nimbilic.quick_cuts import quick_cuts
from Items.Abilities.Standard.ignition import ignition
from Items.Abilities.Standard.stab import stab
from Items.Abilities.Standard.venom_strike import venom_strike
from Items.Materials.wolf_pelt import wolf_pelt
from Items.Weapons.stronias_heirloom import stronias_heirloom
from Saves.save_and_load import save_and_load
from Utility.colors import colors
from Utility.dialogue import dialogue
from Utility.equipment import equipment
from Items.Weapons.wooden_sword import wooden_sword
from Items.Abilities.Brawling.dev_strike import dev_strike

# initiates color for terminal
os.system("color")

# Sets up the console window
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, 3)

dialogue.dia(None, "Welcome to the world of...")
print(
f"\n\n\n\n{colors.LightYellow}"
" _______           _______  _______  _______  _______  _______  _______ _________\n"
"(  ____ \|\     /|(  ____ \(  ____ )(  ____ \(  ____ )(  ____ \(  ____ \\__   __/\n"
"| (    \/| )   ( || (    \/| (    )|| (    \/| (    )|| (    \/| (    \/   ) (   \n"
"| (__    | |   | || (__    | (____)|| |      | (____)|| (__    | (_____    | |   \n"   
"|  __)   ( (   ) )|  __)   |     __)| |      |     __)|  __)   (_____  )   | |   \n"  
"| (       \ \_/ / | (      | (\ (   | |      | (\ (   | (            ) |   | |   \n"   
"| (____/\  \   /  | (____/\| ) \ \__| (____/\| ) \ \__| (____/\/\____) |   | |   \n"   
"(_______/   \_/   (_______/|/   \__/(_______/|/   \__/(_______/\_______)   )_(   \n"
f"{colors.Reset}")
sleep(1.4)

while True:
    answer = gen_menu_num("Pick an option below:", ["Start a new game", "Load your previous game", "Quit the game"], "What would you like to do?", 0)

    if answer == 1:

        cont = gen_menu_yn(f"{colors.LightRed}\nARE YOU SURE? If you had a previous save, it will be OVERWRITED and UNRECOVERABLE!{colors.Reset}")

        if cont:

            # Creates player object from what Character Creator returns
            player = char_create.char_create()

            # Initializes the player's lexicon. We do this so we can avoid circular imports.
            player.lexicon = lexicon(player)

            # Initializes Equipment for first time use.
            equipment(player)

            # Forcefully equip items. Force equipping is the game forcing the player to equip an item, without a prompt.
            equipment.force_equip(stab)
            equipment.force_equip(wooden_sword)

            break

        else:
            pass

    if answer == 2:
        dialogue.dia(None, "Loading your game...")
        player, lexicon = save_and_load.load()
        player.lexicon = lexicon
        lexicon.player = player
        equipment(player)
        player.update_stats(player.level)
        dialogue.dia(None, f"Welcome back, {player.name}!")

        break

    if answer == 3:
        quit(0)

world_map.world_options(player)
