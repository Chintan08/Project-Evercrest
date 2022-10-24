from Core.menus import gen_menu_num
from Utility.colors import colors
from Utility.dialogue import dialogue


class tutorials:

    @staticmethod
    def view():
        options = ["How do Kingdoms work?", "How do the Wilds work?", "How do quests work?", "How does an Ability Master work?", "What are Discovery Points?", "What are Combat Levels?", "Combat for Beginners", "Combat for the Advanced"]
        answer = gen_menu_num("Here is what you'll need to know about Evercrest:", options + [f"Back"], "What would you like to read about?", 0)

        if answer == 1:

            print(f"{colors.LightBlue}How do Kingdoms work?{colors.Reset}\n")

            dialogue.dia(None, "There are 10 Kingdoms in Evercrest. You can see them all in the World Map.")
            dialogue.dia(None, "Each Kingdom has the same menu. However, the individual content of each kingdom is completely unique.")
            dialogue.dia(None, "All kingdoms have a Questgiver, Ability Master, a Wilds section, a unique Marketplace, and the same access to the Lexicon, Armory, and Crafting sections.")
            dialogue.dia(None, "The quests you receive, abilities you can learn, locations you can visit, and the items you can buy are different for each kingdom.")
            dialogue.dia(None, "That's all there is to exploring Evercrest's kingdoms!")

            tutorials.view()

        if answer == 2:

            print(f"{colors.LightBlue}How do the Wilds work?{colors.Reset}\n")

            dialogue.dia(None, "In each Kingdom, you have access to the Wilds. They are, essentially, a Dungeon.")
            dialogue.dia(None, "Each Wilds has 5 unique locations you can visit on every 10th tier. The fifth location is infinite.")
            dialogue.dia(None, "Before each location, there is a boss you have to fight to gain access to the wilds. This boss is designed as a Gatekeeper; if you cannot beat the boss, you will not survive the next location.")
            dialogue.dia(None, "Each location is significantly harder than the last. You will face new enemies, gain new items, and make new important discoveries.")
            dialogue.dia(None, "When you discover a location, you will be able to fast travel to that location.")
            dialogue.dia(None, "After every victory in the Wilds, you will heal a small portion of your health. If you die, you will be kicked out of the Wilds and lose some money!")
            dialogue.dia(None, "That's all there is to the Wilds! If you need help with Combat, there are Combat tutorials you can view.")

            tutorials.view()

        if answer == 3:

            print(f"{colors.LightBlue}How do quests work?{colors.Reset}\n")

            dialogue.dia(None, "Quests are issued by the kingdom's Questgiver.")
            dialogue.dia(None, "Quests can vary in length, difficulty, and reward. Each quest is unique and is rewarding.")
            dialogue.dia(None, "A Questgiver will only give quests if you have met certain requirements. These requirements, for the most part, are secret.")
            dialogue.dia(None, "Quests that are a part of a Storyline offer clues to what may be required next to advance in the Storyline.")
            dialogue.dia(None, "A quest requirement can include: A Discovery Level, a Combat Level, a Previous Quest, if a Location is Discovered, if an Enemy has been killed, and more.")
            dialogue.dia(None, "Make sure to keep talking to the Questgiver!")
            dialogue.dia(None, "The Lexicon shows you how many quests you have completed, and how many quests you've completed pertaining to a location. Use that number to find out if you've completed a kingdom.")
            dialogue.dia(None, "That's all there is to quests!")

            tutorials.view()

        if answer == 4:

            print(f"{colors.LightBlue}How does an Ability Master work?{colors.Reset}")

            dialogue.dia(None, "Ability Masters are in each Kingdom. They work similar to Questgivers in the sense that you will not know the requirements to get an ability.")
            dialogue.dia(None, "Ability Masters give out abilities. The requirements to get these abilities usually have less variance than a quest.")
            dialogue.dia(None, "These requirements usually require certain kills of a native enemy in the Wilds, and a level requirement.")
            dialogue.dia(None, "The abilities given are from an enemy's own arsenal.")
            dialogue.dia(None, "There's no real way to know if you've collected everything from an Ability Master. However, Ability Masters are very predictable in what they'll give.")
            dialogue.dia(None, "Ability Masters drop an ability for almost every enemy in the Wilds.")
            dialogue.dia(None, "That's all there is to Ability Masters!")

            tutorials.view()

        if answer == 5:

            print(f"{colors.LightBlue}What are Discovery Points?{colors.Reset}")

            dialogue.dia(None, "Evercrest has a lot for you to learn about. When you find something new, you Discover it.")
            dialogue.dia(None, "When you discover an item, you jog it down in your Lexicon. This also gives you a Discovery Point.")
            dialogue.dia(None, "In the Lexicon, you can view the items you've discovered, and view the points you have, the points needed to level up, and the total amount of discoveries you've made.")
            dialogue.dia(None, "When you reach the amount of points needed to level up, you will level up and gain extra stats. Your points will reset, and the level requirement will increase.")
            dialogue.dia(None, "The bonuses from leveling up include Healing, and you gain stats depending on the Race you've picked. You can view the stats that will increase on level up in the Armory.")
            dialogue.dia(None, "That's all there is for Discovery Points!")

            tutorials.view()

        if answer == 6:

            print(f"{colors.LightBlue}What are Combat Levels?{colors.Reset}")

            dialogue.dia(None, "A Combat Level is very separate from a normal Level.")
            dialogue.dia(None, "A Combat Level is made up of individual levels from each style.")
            dialogue.dia(None, "When you use a style, you will gain Experience Points towards that style.")
            dialogue.dia(None, "An enemy drops a certain amount of XP depending on its power, and the XP is distributed depending on which style was the most prevalent in that fight.")
            dialogue.dia(None, "Your individual style levels empower your abilities of that style in unique ways. View an Ability's description to see what you'll gain from levels.")
            dialogue.dia(None, "Your total combat level does not do anything for you. It is purely cosmetic.")
            dialogue.dia(None, "That's all there is for Combat Levels!")

            tutorials.view()

        if answer == 7:

            print(f"{colors.LightBlue}Combat for Beginners{colors.Reset}")

            dialogue.dia(None, "Lets talk about Abilities, first.")
            dialogue.dia(None, "You can walk into a fight with 4 abilities. These abilities can be chosen in your equipment.")
            dialogue.dia(None, "When you're in a fight, you have 3 swings available to you. The idea is that you want to chain your abilities together.")
            dialogue.dia(None, "An individual ability may be weak, but when unified with others, that ability may gain all its strength.")
            dialogue.dia(None, "A great fighter knows how to read before they fight. When you get a new ability, it's important to look at a few characteristics.")
            dialogue.dia(None, "An ability description tells you what it does, the formula for its values, its special description, special cooldown, and a unique level bonus.")
            dialogue.dia(None, "When you use an ability, you use its normal function. However, if you meet the ability's Special criteria, you will use the special.")
            dialogue.dia(None, "Specials are incredibly powerful, and have cooldowns. Some specials may cast the attack again, and others may give you more swings!")
            dialogue.dia(None, "Combat is a little deeper than what is shown here. There is another tutorial on advanced combat, if you are looking for more information.")
            dialogue.dia(None, "That's all there is to basic combat!")

            tutorials.view()

        if answer == 8:

            print(f"{colors.LightBlue}Combat for the Advanced{colors.Reset}")

            dialogue.dia(None, "This section is going to look at Style Combos, Effects, and Enemy Behavior.")
            dialogue.dia(None, "When you use all your swings, you may see a Combo message.")
            dialogue.dia(None, "This Combo message is a Style combo. You can read up on the style combo in the Lexicon when you discover it.")
            dialogue.dia(None, "A style combo is a combo that is determined by your first swing, and increases its power depending on the styles casted afterwards.")
            dialogue.dia(None, "Each style in the game has a style combo. Each combo is incredibly unique. The combos are useful in certain situations.")
            dialogue.dia(None, "When against a heavy armored enemy, you may want to use an Elitist combo. When you're low on health, a Resolute combo may help you.")
            dialogue.dia(None, "A combo is powered up by two other styles, depending on the combo. The more you use the other two styles in your swings, the stronger that combo becomes.")
            dialogue.dia(None, "However, each combo has a two round cooldown. But, if you try using the same combo when its on cooldown, it doesn't drop its cooldown. You need to keep track of the cooldowns.")
            dialogue.dia(None, "Now, lets talk about Effects.")
            dialogue.dia(None, "Some abilities can cast an effect. The description of the ability will tell you about the effect, if it has one.")
            dialogue.dia(None, "Some effects can stack, and others cannot. This information is secret. A great fighter needs to learn how to observe the effects in play.")
            dialogue.dia(None, "Some effects can be amplified, and others can be resisted.")
            dialogue.dia(None, "Effects will wear off over time.")
            dialogue.dia(None, "Enemies, like you, know this information too. Some enemies know it a lot better than others.")
            dialogue.dia(None, "The average enemy you'll find is either randomly selecting abilities, or they are slightly aware of their ability's strengths.")
            dialogue.dia(None, "More difficult enemies are smarter, but sometimes more predictable. They can potentially look into what you have, and make guesses on your attack patterns.")
            dialogue.dia(None, "Enemies are not always strong with their statistics; they are strong with their minds. And this is something you will need to observe.")
            dialogue.dia(None, "That's all there is to combat, though! If you have more questions, the information is present in your Lexicon to help you.")

            tutorials.view()

        # back
        if answer == len(options) + 1:
            pass
