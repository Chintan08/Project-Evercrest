from Enemies.Stronia.Bosses.gray_bull import gray_bull
from Enemies.Stronia.baby_golagmite import baby_golagmite
from Enemies.Stronia.dry_rattlesnake import dry_rattlesnake
from Enemies.Stronia.mountain_wolf import mountain_wolf
from Items.Abilities.Elitist.bull_swipe import bull_swipe
from Items.Abilities.Nimbilic.quick_cuts import quick_cuts
from Items.Abilities.Resolute.body_bash import body_bash
from Items.Abilities.Standard.venom_strike import venom_strike
from Utility.colors import colors
from Utility.dialogue import dialogue
from Utility.equipment import equipment


class kaero:

    name = f"{colors.LightYellow}Master Kaero{colors.Reset}"
    desc = "Kaero is an Ability Master for Stronia. Ever since he had mutated into a Terranox, he had learnt how to effectively use his fists. And now he looks to teach you the same." \
           "\nHe tends to teach heavier Elitist/Brawler type abilities, but he is also well rounded."

    type = "character"

    abilities = [quick_cuts, body_bash, venom_strike, bull_swipe]

    @staticmethod
    def give_ability(player):

        kills = player.lexicon.compress_kills()

        if not player.lexicon.is_discovered(kaero):
            dialogue.dia(None, "As you walk on the cliffsides of the kingdom, you come across a Terranox, absolutely destroying pure stone with just his fists!")
            dialogue.dia(player.name, "Uhh... who are you?")
            dialogue.dia(None, f"The Terranox stopped his fist-based rampage, and looked at you.")
            dialogue.dia(f"{colors.LightBlue}???{colors.Reset}", "Hm?")
            dialogue.dia(None,
                         "You are surprised he did not fling you off the mountain for interrupting his guilty pleasure.")
            dialogue.dia(player.name, "I'm new here. I'm guessing by the whole macho training thing... are you an Ability Master?")
            dialogue.dia(f"{colors.LightBlue}???{colors.Reset}",
                         f"Is it that obvious? I am {kaero.name}, the Ability Master for Stronia.")

            player.lexicon.update_discovery(kaero)

            dialogue.dia(kaero.name,
                         "I can teach you all that the enemies of Stronia know, and perhaps even more!")
            dialogue.dia(kaero.name,
                         "Prove that to me by fighting off different enemies around Stronia, and come back to me.")

        # QUICK CUTS
        if mountain_wolf.name in player.enemies_killed and kills[mountain_wolf.name] >= 5:
            dialogue.dia(kaero.name, f"You sure have a lot of scratches on your face.")
            dialogue.dia(player.name, "Mountain Wolves aren't nice! Who knew?!")
            dialogue.dia(kaero.name, f"Wolves cut really quickly. I can show you how to do that.")

            equipment.add_to_inv(kaero.abilities[0])

            dialogue.dia(player.name, "Now I get to fight fire with fire!")

        # TODO: replace with adult golagmite
        # # BODY BASH
        # if baby_golagmite.name in player.enemies_killed and player.enemies_killed[baby_golagmite.name] >= 5:
        #     dialogue.dia(kaero.name, f"You look a bit... frustrated.")
        #     dialogue.dia(player.name, "Yeah! Damn Baby Golagmites keep slamming into me and it hurts like crazy!")
        #     dialogue.dia(kaero.name, f"Don't be upset by things better than you.")
        #     dialogue.dia(player.name, "Wha-")
        #     dialogue.dia(kaero.name, f"Let me explain to you the technique behind it. It's quite interesting!")
        #     dialogue.dia(kaero.name, f"Body Bashing uses your weight to deal most of the damage. And if they have less armor than you, it's even more effective! Let me show you.")
        #
        #     equipment.add_to_inv(kaero.abilities[1])
        #
        #     dialogue.dia(kaero.name, f"Better start bulking.")

        # VENOM STRIKE
        if dry_rattlesnake.name in player.enemies_killed and kills[dry_rattlesnake.name] >= 5:
            dialogue.dia(kaero.name, f"Are those bite marks?")
            dialogue.dia(player.name, "Yep. Damn Rattlesnakes and their poison!")
            dialogue.dia(kaero.name, "Your blade can do the same thing. Let me show you.")

            equipment.add_to_inv(kaero.abilities[2])

            dialogue.dia(kaero.name, "Please don't bite a snake.")

        # BULL SWIPE
        if gray_bull.name in player.enemies_killed and player.level >= 3:
            dialogue.dia(kaero.name, f"I have heard you killed a mighty Gray Bull!")
            dialogue.dia(player.name, f"Yeah, it wasn't pretty, but I sure did it!")
            dialogue.dia(kaero.name, f"I want to teach you something. When the bull swipes his mighty horns at you, you may feel that you cannot match that power.")
            dialogue.dia(kaero.name, f"You need to understand your weapon is your horn! You can match that power, and you can rise above it! Let me show you.")

            equipment.add_to_inv(kaero.abilities[3])

            dialogue.dia(kaero.name, f"And with this, I hope your next encounter is a bit prettier.")

        dialogue.dia(kaero.name, "There's not much I can teach you right now. Come back later if you think you are ready.")

