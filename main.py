from colored import fore, style
import os
from Core.character_creator import char_create
from Core.lexicon import lexicon
from Core.world_map import world_map
from Utility.equipment import equipment
from Items.Weapons.wooden_sword import wooden_sword
from Items.Weapons.stronias_heirloom import stronias_heirloom
from Items.Abilities.stab import stab
from Items.Abilities.dev_punch import dev_punch
from Items.Abilities.cinderblade import cinderblade

# initiates color for terminal
os.system("color")

player = char_create.char_create()
player.lexicon = lexicon(player)
equipment(player)

equipment.force_equip(stab)
equipment.force_equip(dev_punch)
equipment.force_equip(stronias_heirloom)
equipment.force_equip(cinderblade)

world_map.world_options(player)