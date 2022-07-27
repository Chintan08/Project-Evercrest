import os
from Core.character_creator import char_create
from Core.lexicon import lexicon
from Core.menus import gen_menu_yn
from Core.world_map import world_map
from Items.Abilities.Resolute.body_bash import body_bash
from Items.Abilities.Nimbilic.quick_cuts import quick_cuts
from Items.Abilities.Standard.ignition import ignition
from Items.Abilities.Standard.stab import stab
from Items.Abilities.Standard.venom_strike import venom_strike
from Items.Materials.wolf_pelt import wolf_pelt
from Items.Weapons.stronias_heirloom import stronias_heirloom
from Saves.save_and_load import save_and_load
from Utility.equipment import equipment
from Items.Weapons.wooden_sword import wooden_sword
from Items.Abilities.Brawling.dev_strike import dev_strike

# initiates color for terminal
os.system("color")

ans = gen_menu_yn("Would you like to load your game?")

if ans:
    player, lexicon = save_and_load.load()
    player.lexicon = lexicon
    lexicon.player = player
    equipment(player)
    player.update_stats(player.level)

else:
    # Creates player object from what Character Creator returns
    player = char_create.char_create()

    # Initializes the player's lexicon. We do this so we can avoid circular imports.
    player.lexicon = lexicon(player)

    # Initializes Equipment for first time use.
    equipment(player)

    # Forcefully equip items. Force equipping is the game forcing the player to equip an item, without a prompt.
    equipment.force_equip(stab)
    equipment.force_equip(wooden_sword)

world_map.world_options(player)
