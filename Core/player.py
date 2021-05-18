
class player:

    # name of the player
    name = ""
    type = "player"

    # race of the player, is Object
    race = None

    # STATS:
    maxhp = 0.0
    hp = 0.0
    dmg = 0.0
    armor = 0.0
    armor_percent = 0.0
    crc = 0.0
    speed = 0.0

    raw_armor = 0.0
    raw_armor_percent = 0.0
    raw_maxhp = 0.0
    raw_dmg = 0.0
    raw_crc = 0.0
    raw_speed = 0.0

    immune_to_burn = False

    money = 0

    # lexicon/combat related:

    level = 0

    weapon = None
    helmet = None
    chestplate = None
    leggings = None
    boots = None
    accessory = None
    abilities = []
    equipped = [weapon, helmet, chestplate, leggings, boots, accessory]

    weapons = []
    helmets = []
    chestplates = []
    leggings_inv = []
    boots_inv = []
    ability_inv = []
    accessory_inv = []
    materials = []
    inventory = {"weapon": weapons, "helmet": helmets, "chestplate": chestplates, "leggings": leggings_inv, "boots": boots_inv, "ability": ability_inv, "accessory": accessory_inv, "material": materials}

    # this xp section is individual combat experience, gained from abilities
    dueling_xp = 0.0
    resolute_xp = 0.0
    elitist_xp = 0.0
    brawling_xp = 0.0
    standard_xp = 0.0
    elder_xp = 0.0
    flowing_xp = 0.0
    nimbilic_xp = 0.0

    # stores the object of Lexicon, it does not have a lexicon until player is initialized on first time setup
    lexicon = None

    enemies_killed = {}

    current_quests = []

    # TODO: armor percent
    # this constructor is called from character_creator, gets name and race from there.
    def __init__(self, name, race):
        self.name = name
        self.race = race

        # first time initialization
        self.raw_maxhp = race.hp + 10000
        self.hp = self.raw_maxhp
        self.raw_dmg = race.dmg
        self.raw_armor = race.armor
        self.raw_armor_percent = 0.0
        self.raw_crc = race.crc
        self.raw_speed = race.speed
        self.immune_to_burn = race.immune_to_burn

    def update_stats(self, level):

        if level > self.level:
            self.raw_maxhp += self.race.hp_scale
            self.raw_dmg += self.race.dmg_scale
            self.raw_armor += self.race.armor_scale
            self.raw_armor_percent += self.race.armor_percent_scale
            self.raw_crc += self.race.crc_scale
            self.raw_speed += self.race.spd_scale

        # gets weapon stats, fists (no weapon) is handled from equipment
        self.dmg = self.weapon.dmg
        self.maxhp = self.weapon.hp
        self.speed = self.weapon.speed
        self.armor = self.weapon.armor
        self.armor_percent = self.weapon.armor_percent
        self.crc = self.weapon.crc

        self.dmg += self.helmet.dmg
        self.maxhp += self.helmet.hp
        self.speed += self.helmet.speed
        self.armor += self.helmet.armor
        self.armor_percent += self.helmet.armor_percent
        self.crc += self.helmet.crc

        self.dmg += self.chestplate.dmg
        self.maxhp += self.chestplate.hp
        self.speed += self.chestplate.speed
        self.armor += self.chestplate.armor
        self.armor_percent += self.chestplate.armor_percent
        self.crc += self.chestplate.crc

        self.dmg += self.leggings.dmg
        self.maxhp += self.leggings.hp
        self.speed += self.leggings.speed
        self.armor += self.leggings.armor
        self.armor_percent += self.leggings.armor_percent
        self.crc += self.leggings.crc

        self.dmg += self.boots.dmg
        self.maxhp += self.boots.hp
        self.speed += self.boots.speed
        self.armor += self.boots.armor
        self.armor_percent += self.boots.armor_percent
        self.crc += self.boots.crc

        self.dmg += self.accessory.dmg
        self.crc += self.accessory.crc
        self.maxhp += self.accessory.hp
        self.armor += self.accessory.armor
        self.armor_percent += self.accessory.armor_percent
        self.speed += self.accessory.speed

        self.dmg += self.raw_dmg
        self.maxhp += self.raw_maxhp
        self.speed += self.raw_speed
        self.armor += self.raw_armor
        self.armor_percent += self.raw_armor_percent
        self.crc += self.raw_crc

        # TODO: This line makes it so you heal everytime you equip something; we don't want that
        if level > self.level:
            self.hp = self.maxhp
            self.level += 1

    # when you need to return back to the location's menu prompt, this is how
    # location can either be a place, or 0. If it's zero, you are travelling to the location's return point.
    # if location is not zero, you are setting a return point.
    def returning(self, location):

        # if you're not going, you're setting a location point
        if location != 0:
            self.old_location = location

        # if you're going, you travel to the old location
        if location == 0:
            self.old_location.menu_prompt()

    # used to return to the world map
    def return_to_world(self, set):
        if set != 0:
            self.old_place = set
        if set == 0:
            self.old_place.world_options(self)
