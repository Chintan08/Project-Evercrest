from Utility.colors import colors
from Utility.dialogue import dialogue


class player(object):

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

    xp_bonus = 0.0
    raw_xp_bonus = 0.0

    raw_fire_resistance = 0.0
    raw_shock_resistance = 0.0

    fire_resistance = 0.0
    shock_resistance = 0.0
    poison_amp = 0.0

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
    last_equipped = equipped  # used in update stats

    inventory = {"weapon": [], "helmet": [], "chestplate": [], "leggings": [], "boots": [], "ability": [], "accessory": [], "material": []}

    # this xp section is individual combat experience, gained from abilities
    # xp requirements to level up

    combat_req = {"dueling": 30, "eldric": 30, "nimbilic": 30, "resolute": 30,
                  "elitist": 30, "standard": 30,
                  "brawler": 30}

    combat_xp = {"dueling": 0.0, "eldric": 0.0, "nimbilic": 0.0, "resolute": 0.0, "elitist": 0.0, "standard": 0.0,
                 "brawler": 0.0}

    combat_level = {"dueling": 0, "eldric": 0, "nimbilic": 0, "resolute": 0,
                    "elitist": 0, "standard": 0,
                    "brawler": 0}

    total_combat_level = 0

    enemies_killed = []

    current_quests = []
    completed_quests = []

    # stores the object of Lexicon, it does not have a lexicon until player is initialized on first time setup
    lexicon = None

    # this constructor is called from character_creator, gets name and race from there.
    def __init__(self, name, race):
        self.name = name
        self.race = race

        # first time initialization
        self.raw_maxhp = race.hp
        self.hp = self.raw_maxhp
        self.raw_dmg = race.dmg
        self.raw_armor = race.armor
        self.raw_armor_percent = race.armor_percent
        self.raw_crc = race.crc
        self.raw_speed = race.speed
        self.raw_xp_bonus = race.xp_bonus
        self.fire_resistance = race.fire_resistance
        self.shock_resistance = race.shock_resistance

    def update_stats(self, level):

        if level > self.level:
            self.raw_maxhp += self.race.hp_scale
            self.raw_dmg += self.race.dmg_scale
            self.raw_armor += self.race.armor_scale
            self.raw_armor_percent += self.race.armor_percent_scale
            self.raw_crc += self.race.crc_scale
            self.raw_speed += self.race.spd_scale
            self.raw_xp_bonus += self.race.xp_scale
            self.raw_fire_resistance += self.race.fire_resistance_scale
            self.raw_shock_resistance += self.race.shock_resistance_scale
            self.level += 1

        # goes through all calculations again, as if your cripple is being cleansed too
        # gets weapon stats, fists (no weapon) is handled from equipment
        self.dmg = self.weapon.dmg
        self.maxhp = self.weapon.hp
        self.speed = self.weapon.speed
        self.armor = self.weapon.armor
        self.armor_percent = self.weapon.armor_percent
        self.crc = self.weapon.crc
        self.xp_bonus = self.weapon.xp_bonus
        self.fire_resistance = self.weapon.fire_resistance
        self.shock_resistance = self.weapon.shock_resistance
        self.poison_amp = self.weapon.poison_amp

        self.dmg += self.helmet.dmg
        self.maxhp += self.helmet.hp
        self.speed += self.helmet.speed
        self.armor += self.helmet.armor
        self.armor_percent += self.helmet.armor_percent
        self.crc += self.helmet.crc
        self.xp_bonus += self.helmet.xp_bonus
        self.fire_resistance += self.helmet.fire_resistance
        self.shock_resistance += self.helmet.shock_resistance
        self.poison_amp = self.helmet.poison_amp

        self.dmg += self.chestplate.dmg
        self.maxhp += self.chestplate.hp
        self.speed += self.chestplate.speed
        self.armor += self.chestplate.armor
        self.armor_percent += self.chestplate.armor_percent
        self.crc += self.chestplate.crc
        self.xp_bonus += self.chestplate.xp_bonus
        self.fire_resistance += self.chestplate.fire_resistance
        self.shock_resistance += self.chestplate.shock_resistance
        self.poison_amp = self.chestplate.poison_amp

        self.dmg += self.leggings.dmg
        self.maxhp += self.leggings.hp
        self.speed += self.leggings.speed
        self.armor += self.leggings.armor
        self.armor_percent += self.leggings.armor_percent
        self.crc += self.leggings.crc
        self.xp_bonus += self.leggings.xp_bonus
        self.fire_resistance += self.leggings.fire_resistance
        self.shock_resistance += self.leggings.shock_resistance
        self.poison_amp = self.leggings.poison_amp

        self.dmg += self.boots.dmg
        self.maxhp += self.boots.hp
        self.speed += self.boots.speed
        self.armor += self.boots.armor
        self.armor_percent += self.boots.armor_percent
        self.crc += self.boots.crc
        self.xp_bonus += self.boots.xp_bonus
        self.fire_resistance += self.boots.fire_resistance
        self.shock_resistance += self.boots.shock_resistance
        self.poison_amp = self.boots.poison_amp

        self.dmg += self.accessory.dmg
        self.crc += self.accessory.crc
        self.maxhp += self.accessory.hp
        self.armor += self.accessory.armor
        self.armor_percent += self.accessory.armor_percent
        self.speed += self.accessory.speed
        self.xp_bonus += self.accessory.xp_bonus
        self.fire_resistance += self.accessory.fire_resistance
        self.shock_resistance += self.accessory.shock_resistance
        self.poison_amp = self.accessory.poison_amp

        self.dmg += self.raw_dmg
        self.maxhp += self.raw_maxhp
        self.speed += self.raw_speed
        self.armor += self.raw_armor
        self.armor_percent += self.raw_armor_percent
        self.crc += self.raw_crc
        self.xp_bonus += self.raw_xp_bonus
        self.fire_resistance += self.raw_fire_resistance
        self.shock_resistance += self.raw_shock_resistance

        if self.last_equipped != self.equipped:
            self.hp = self.maxhp  # heal up to max

        if level > self.level:
            self.hp = self.maxhp

        # this variable is used to compare if equipment changed or not
        self.last_equipped = self.equipped

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

    # called from Combat, this method gives the player combat XP depending on what was used
    def give_combat_xp(self, style, xp):

        for styles in self.combat_xp:

            if styles == style:

                self.combat_xp[styles] += xp
                dialogue.dia(None, f"Your {colors.Yellow}{styles.upper()}{colors.Reset} style just got {colors.LightCyan}{xp}{colors.Reset} XP!")

                while self.combat_xp[styles] >= self.combat_req[styles]:

                    self.combat_level[styles] += 1
                    self.total_combat_level += 1

                    dialogue.dia(None, f"{colors.Yellow}You've leveled up your {colors.Magenta}{styles.upper()}{colors.Yellow} style combat level! You will now be better with abilities of that style. \n"
                                       f"{colors.LightGreen}You are now level {colors.LightCyan}{self.combat_level[styles]}{colors.LightGreen}! Your total combat level is now {colors.LightCyan}{self.total_combat_level}{colors.Reset}.")

                    self.combat_xp[styles] = self.combat_xp[styles] - self.combat_req[styles]
                    self.combat_req[styles] = int(self.combat_req[styles] * 1.3)
