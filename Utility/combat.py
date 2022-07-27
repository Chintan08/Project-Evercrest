from random import randint
from Utility.colors import colors
from Utility.damage import damage
from Utility.dialogue import dialogue
from Utility.healthbar import healthbar
from Core.menus import gen_menu_num
from Items.Abilities.blank import blank
from Utility.equipment import equipment
from time import sleep


class combat:

    pdmg = 0
    pdef = 0
    pcrc = 0
    pspd = 0

    edmg = 0
    edef = 0
    ecrc = 0
    espd = 0

    mobs = []

    effects = {"player": [], "enemy": []}
    player_list = []
    enemy_list = []

    swing = 3
    swings = []
    styles = []

    delay_list = {"player": {}, "enemy": {}}
    round = 0

    ##############################################
    # MAIN METHODS #
    ##############################################

    # Runs through a pre-check. This includes:
    # Resetting ability values
    # Calling on save_instance()
    # Sorting mob speeds
    # Calls on battle which then calls on post which then returns back for winner
    @staticmethod
    def precheck(player, enemy):

        player.update_stats(player.level)

        combat.mobs = [player, enemy]
        combat.mobs.sort(key=combat.by_speed, reverse=True)

        combat.player_list = []
        combat.enemy_list = []

        for ability in player.abilities:
            if ability is not blank:
                combat.player_list.append(ability())

        for ability in enemy.abilities:
            if ability is not blank:
                combat.enemy_list.append(ability())

        combat.swing = 3
        combat.swings = []
        combat.styles = []

        combat.delay_list["player"] = {}
        combat.delay_list["enemy"] = {}

        # if the enemy has not been discovered, we run through a lexicon update
        # if not, print a basic prompt
        names = [enemy.name for enemy in player.lexicon.lexicon_dict["enemy"]]
        if enemy.name not in names:
            player.lexicon.update_discovery(enemy)

        else:
            dialogue.dia(None, f"\n{colors.LightCyan}You come across a{colors.Reset}{colors.LightRed} {enemy.name}{colors.Reset}.\n")

        # here we look at speeds and compare them
        # self explanatory
        if combat.mobs[0] != player:
            print(f"{colors.Red}{enemy.name}{colors.Reset} is {colors.Blue}faster{colors.Reset} than {colors.Green}you{colors.Reset}! They get the move on you.")

        else:
            print(f"{colors.Green}You're{colors.Reset} {colors.Blue}faster{colors.Reset} than {colors.Red}{enemy.name}{colors.Reset}! You get the move.")

        return combat.battle(player, enemy)

    # The main battle that handles battling
    # This will be the method where swings and other variables are changed
    # We call gen_combo() here
    # When hp = 0, post() is called
    @staticmethod
    def battle(player, enemy):
        combat.round = 1

        while True:

            # in case swings need to be incremented, this is put here so we can add to 3 instead of it getting replaced like before
            combat.swing = 3

            for ability in combat.player_list:
                ability.cur_cd -= 1

            for ability in combat.enemy_list:
                ability.cur_cd -= 1

            for index in range(0, len(combat.effects["player"]))[::-1]:
                combat.effects["player"][index].constant(combat)

            for index in range(0, len(combat.effects["enemy"]))[::-1]:
                combat.effects["enemy"][index].constant(combat)

            for mob in combat.mobs:

                # reset before the round because abilities may want to interact with this through effects (see prediction)
                combat.styles = []
                combat.swings = []

                combat.print_healthbars(player, enemy)

                if player.hp <= 0.0:
                    return combat.post(player, enemy, False)

                elif enemy.hp <= 0.0:
                    return combat.post(player, enemy, True)

                if mob == player:

                    while combat.swing > 0:
                        sleep(0.2)
                        ans = gen_menu_num(
                            f"{colors.Blue}What do you want to do, {colors.LightGreen}{player.name}{colors.Blue}?\n{colors.Magenta}You have {colors.Yellow}{combat.swing}{colors.Magenta} swings remaining.{colors.Reset}",
                            [ability.name for ability in combat.player_list] + [f"Pass this round"],
                            "What are you going to do?", 0)

                        if ans == len(combat.player_list) + 1:
                            print(f"\n{colors.Green}You've passed this turn.{colors.Reset}\n")
                            break

                        else:
                            ability = combat.player_list[ans - 1]

                            print(f"{player.name} has cast {ability.name}!\n")

                            combat.swings.append(ability)
                            combat.styles.append(ability.style)

                            ability.action(combat, player, enemy)
                            ability.special(combat, player, enemy)

                        combat.swing -= 1

                    # TODO: Abilities that need the full swing set to proc their special need to be able to check after the loop is over. Make sure no abilities have issues with proccings specials.
                    if len(combat.swings) != 0:
                        for ability in combat.player_list:
                            ability.special(combat, player, enemy)

                    combat.gen_combo(player, enemy)

                else:

                    combat.swing = 3

                    while combat.swing > 0:
                        print(f"\n\n{colors.Yellow}{enemy.name} is thinking...{colors.Reset}\n"
                              f"{colors.Magenta}They have {colors.Yellow}{combat.swing}{colors.Magenta} swings remaining.{colors.Reset}\n\n")

                        sleep(2)

                        ability = enemy.choose(combat)

                        print(f"{colors.LightRed}{enemy.name}{colors.Reset} cast {ability.name}!\n")

                        combat.swings.append(ability)
                        combat.styles.append(ability.style)

                        ability.action(combat, enemy, player)
                        ability.special(combat, enemy, player)

                        combat.swing -= 1

                    # TODO: Abilities that need the full swing set to proc their special need to be able to check after the loop is over. Make sure no abilities have issues with proccings specials.
                    if len(combat.swings) != 0:
                        for ability in combat.enemy_list:
                            ability.special(combat, enemy, player)

                    combat.gen_combo(enemy, player)

                # reset after every iteration
                combat.swing = 3

    # This returns a winner and a loser
    # This method also handles enemy drops and money losses
    # Calls on save_instance to rewind
    @staticmethod
    def post(player, enemy, victory):

        # this heals player if you lost
        combat.save_instance(player, enemy, True)

        if victory:
            dialogue.dia(None, f"\n{colors.Yellow}You defeated {colors.Red}{enemy.name}{colors.Reset}!")
            sleep(.6)
            print(f"\n{colors.Yellow}Let's see what {enemy.name} drops!{colors.Reset}")
            sleep(1)

            # dictates how many drops you get
            num = 1
            items = 0
            for index in range(0, 5): # up to 5 items can be dropped
                chose = randint(1, num)
                if chose == num:
                    items += 1
                    num *= 3
                else:
                    break

            # drops items depending on number from above
            for index in range(0, items):
                item = enemy.drop()

                if item is None:
                    print(f"\n{colors.Red}{enemy.name} dropped nothing! No more items will be dropped.{colors.Reset}\n")
                    break

                else:
                    print(f"\n{colors.Red}{enemy.name}{colors.Reset} dropped {item.name}!\n")

                    equipment.add_to_inv(item)

                    print(f"{colors.Yellow}...{colors.Reset}")
                    sleep(3)

            # drops money
            amount = enemy.money()
            print(
                f"\n{colors.Red}{enemy.name}{colors.Reset} dropped {colors.LightGreen}${amount}{colors.Reset}! You now have {colors.Green}${player.money + amount}{colors.Reset}.\n")
            player.money += amount

            # drops XP
            xp = randint(enemy.xp_drop_range[0], enemy.xp_drop_range[1])
            total_damage = 0

            dialogue.dia(None, f"{enemy.name} has dropped {colors.LightCyan}{xp}{colors.Reset} XP!")
            damage_values = damage.get_values()

            for style in damage.get_values():
                if damage_values[style] > 0:
                    total_damage += damage.get_values()[style]

            for style in damage.get_values():
                if damage_values[style] > 0:
                    player.give_combat_xp(style, int((damage.get_values()[style]/total_damage) * xp * player.xp_bonus))

            damage.clear_values()

            # updates kill list
            player.enemies_killed.append(enemy.name)

            return True  # whoever called on this class knows that you won

        # PLAYER LOST
        else:

            # drops money when dead
            print(
                f"\n{colors.Red}You blacked out{colors.Reset}. You dropped {colors.Green}${.12 * player.money}{colors.Red} when you fell!{colors.Reset}"
                f"\nYou now have {colors.LightGreen}${player.money}{colors.Reset}.")
            player.money -= (.12 * player.money)

            return False  # whoever called on this class knows that you lost

    ##############################################
    # UTILITY METHODS #
    ##############################################

    # A method used to return a speed of a mob.
    @staticmethod
    def by_speed(mob):
        return mob.speed

    # Save an instance of all stats from both the enemy and the player.
    # This is so we can "rewind" specific stats.
    # The count variable lets us know if we are looking to set or rewind.
    # TODO: figure out if this works
    @staticmethod
    def save_instance(player, enemy, rewind):

        if rewind == False:

            combat.pdmg = player.dmg
            combat.pdef = player.defense
            combat.pcrc = player.crit_chance
            combat.pspd = player.speed

        else:

            del enemy

            player.speed = combat.pspd
            player.dmg = combat.pdmg
            player.defense = combat.pdef
            player.crit_chance = combat.pcrc

            combat.effects["player"] = []
            combat.effects["enemy"] = []

            # if you lost, your hp is healed, but if not dead, no heal
            if player.hp <= 0:
                player.hp = player.maxhp

    # Generate a combo by looking at:
    # The starting type of the combo, to set what reward you get
    # The starting type makes it so you cannot do that same combo twice in a row
    # Then it looks at the rest of the combo, and adds multipliers depending on strength.
    @staticmethod
    def gen_combo(caster, casted):
        #print(combat.delay_list)

        if caster.type == "player":

            i_list = []

            for style in combat.delay_list["player"]:

                # only remove the duration if you haven't done it already
                if combat.styles[0] not in combat.delay_list[caster.type]:
                    combat.delay_list["player"][style] -= 1

                if combat.delay_list["player"][style] <= 0:

                    i_list.append(style)

            for index in i_list:
                del combat.delay_list["player"][index]

        else:

            i_list = []

            for style in combat.delay_list["enemy"]:

                # only remove the duration if you haven't done it already
                if combat.styles[0] not in combat.delay_list[caster.type]:
                    combat.delay_list["enemy"][style] -= 1

                if combat.delay_list["enemy"][style] <= 0:

                    i_list.append(style)

            for index in i_list:
                del combat.delay_list["enemy"][index]

        #print(combat.delay_list)

        if len(combat.styles) > 0:
            if combat.styles[0] not in combat.delay_list[caster.type]:
                sleep(.5)
                combat.styles[0].action(combat, caster, casted)
                combat.delay_list[caster.type][combat.styles[0]] = 2
                if caster.type == "player":
                    caster.lexicon.update_discovery(combat.styles[0])

        #print(combat.delay_list)

    # this method is only called on when an effect's duration is 0. not every time
    @staticmethod
    def kill_effect():

        for effects in range(len(combat.effects["player"]))[::-1]:
            if combat.effects["player"][effects].duration <= 0:
                del combat.effects["player"][effects]

        for effects in range(len(combat.effects["enemy"]))[::-1]:
            if combat.effects["enemy"][effects].duration <= 0:
                del combat.effects["enemy"][effects]

    @staticmethod
    def print_healthbars(player, enemy):

        print(f"\n{player.name}'s HP: ")
        sleep(.2)
        healthbar.animated_hp_bar(24, player.hp, player.maxhp)
        sleep(.2)
        print(f"({player.hp} / {player.maxhp}) \n")

        print(f"{enemy.name}'s HP: ")
        sleep(.2)
        healthbar.animated_hp_bar(24, enemy.hp, enemy.maxhp)
        sleep(.2)
        print(f"({enemy.hp} / {enemy.maxhp})")

    @staticmethod
    def get_effect_list(cast):

        effects = []
        for effect in combat.effects[cast.type]:
            effects.append(effect.type)

        return effects
