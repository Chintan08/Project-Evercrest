from Utility.colors import colors
from Enemies.Stronia.golagmite import golagmite


class golagmite_infestation:
    discovered = False

    name = "Golagmite Infestation"
    desc = "Bjorne has heard that there have been heavy Golagmite Infestations. Clean out 2 of them."
    undiscovered_desc = "The Stronia People have been getting mad at the Golagmites running rampant. Help them out."

    starting = 0
    completed = False

    type = "quest"

    lvl_req = 0
    location = "Stronia"

    started = False

    @staticmethod
    def start(player):

        if not golagmite_infestation.started:

            golagmite_infestation.started = True

            if golagmite.name not in player.enemies_killed:
                golagmite_infestation.starting = 0

            else:
                golagmite_infestation.starting = player.enemies_killed[golagmite.name]

            player.returning(0)

        else:
            golagmite_infestation.check(player)

    @staticmethod
    def check(player):

        if golagmite.name not in player.enemies_killed:
            print(f"\n{colors.Red}You haven't killed a single Golagmite!{colors.Reset}\n")
            player.returning(0)

        elif player.enemies_killed[golagmite.name] - golagmite_infestation.starting == 2:
            golagmite_infestation.give_reward(player)
            player.returning(0)

        else:
            print(f"\n{colors.LightRed}You haven't killed enough Golagmites...{colors.Reset}\n")
            player.returning(0)

    # gives the quest reward
    # need to use this method because we do not want to differentiate between reward types.
    @staticmethod
    def give_reward(player):

        print(f"\nYou've been given {colors.Green}$50{colors.Reset} dollars for your hard work.\n")
        player.money += 50

        golagmite_infestation.completed = True

        for index in range(0, len(player.current_quests)):
            if player.current_quests[index] == golagmite_infestation:
                del player.current_quests[index]
                break
