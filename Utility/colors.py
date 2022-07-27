# Escape sequences used for colors in terminals


class colors:
    Black = "\033[30m"
    Red = "\033[31m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[36m"
    White = "\033[37m"
    Reset = "\033[0m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"

    bg_Black = "\033[40m"
    bg_Red = "\033[41m"
    bg_Green = "\033[42m"
    bg_Yellow = "\033[43m"
    bg_Blue = "\033[44m"
    bg_Magenta = "\033[45m"
    bg_Cyan = "\033[46m"
    bg_White = "\033[47m"
    bg_Reset = "\033[0m"

    # If you use this in an f-string, make sure to use single quotes for the inputs
    @staticmethod
    def wrap_color(string, color):
        string = str(string)
        return getattr(colors, color) + string + colors.Reset
