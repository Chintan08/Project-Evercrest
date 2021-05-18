from Utility.colors import colors


class blank:

    type = "ability"
    combat_type = "standard"

    discovered = False

    name = f"{colors.White}None{colors.Reset}"
    desc = f"You have no ability equipped here."

    def __init__(self):
        pass
