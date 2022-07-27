import jsonpickle
import json

class save_and_load:

    @staticmethod
    def save(player_obj):

        player_object = jsonpickle.encode(player_obj, keys=True)
        player_inventory = jsonpickle.encode(player_obj.inventory, keys=True)
        player_req = jsonpickle.encode(player_obj.combat_req, keys=True)
        player_xp = jsonpickle.encode(player_obj.combat_xp, keys=True)
        player_level = jsonpickle.encode(player_obj.combat_level, keys=True)
        player_killed = jsonpickle.encode(player_obj.enemies_killed, keys=True)
        player_current_quests = jsonpickle.encode(player_obj.current_quests)
        player_completed_quests = jsonpickle.encode(player_obj.completed_quests)

        lexicon_object = jsonpickle.encode(player_obj.lexicon, keys=True)
        discovered = jsonpickle.encode(player_obj.lexicon.lexicon_dict)

        with open("Saves/player1.json", "w") as f:
            json.dump(player_object, f)

        with open("Saves/inventory1.json", "w") as f:
            json.dump(player_inventory, f)

        with open("Saves/req1.json", "w") as f:
            json.dump(player_req, f)

        with open("Saves/xp1.json", "w") as f:
            json.dump(player_xp, f)

        with open("Saves/level1.json", "w") as f:
            json.dump(player_level, f)

        with open("Saves/kills1.json", "w") as f:
            json.dump(player_killed, f)

        with open("Saves/current1.json", "w") as f:
            json.dump(player_current_quests, f)

        with open("Saves/completed1.json", "w") as f:
            json.dump(player_completed_quests, f)

        with open("Saves/lexicon1.json", "w") as f:
            json.dump(lexicon_object, f)

        with open("Saves/discovery1.json", "w") as f:
            json.dump(discovered, f)

    @staticmethod
    def load():

        with open("Saves/player1.json", "r") as f:
            read = json.load(f)

        with open("Saves/inventory1.json", "r") as f:
            inventory = json.load(f)

        with open("Saves/req1.json", "r") as f:
            req = json.load(f)

        with open("Saves/xp1.json", "r") as f:
            xp = json.load(f)

        with open("Saves/level1.json", "r") as f:
            level = json.load(f)

        with open("Saves/kills1.json", "r") as f:
            kills = json.load(f)

        with open("Saves/current1.json", "r") as f:
            current = json.load(f)

        with open("Saves/completed1.json", "r") as f:
            completed = json.load(f)

        with open("Saves/lexicon1.json", "r") as f:
            readL = json.load(f)

        with open("Saves/discovery1.json", "r") as f:
            discovered = json.load(f)

        # re-assemble player
        loaded = jsonpickle.decode(read, keys=True)
        loaded.inventory = jsonpickle.decode(inventory, keys=True)
        loaded.combat_req = jsonpickle.decode(req, keys=True)
        loaded.combat_xp = jsonpickle.decode(xp, keys=True)
        loaded.combat_level = jsonpickle.decode(level, keys=True)
        loaded.enemies_killed = jsonpickle.decode(kills)
        loaded.current_quests = jsonpickle.decode(current)
        loaded.completed_quests = jsonpickle.decode(completed)

        # re-assemble the lexicon
        loaded_lex = jsonpickle.decode(readL, keys=True)
        loaded_lex.lexicon_dict = jsonpickle.decode(discovered, keys=True)

        return loaded, loaded_lex
