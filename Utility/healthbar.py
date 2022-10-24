from Utility.colors import colors
from time import sleep


class healthbar:

    @staticmethod
    def hp_bar(length, var, max_var):
        bar = ""
        ratio = float(var / max_var)
        chars_printed = 0

        bar += colors.Green
        while (float(chars_printed / length)) < ratio:
            bar += "█"
            chars_printed += 1

        bar += colors.Red
        while chars_printed < length:
            bar += "█"
            chars_printed += 1

        bar += colors.Reset
        return bar

    @staticmethod
    def animated_hp_bar(length, var, max_var):
        ratio = float(var / max_var)
        chars_printed = 0

        print(colors.Green, end="")
        while (float(chars_printed / length)) < ratio:
            sleep(.02)
            print("█", end="", flush=True)
            chars_printed += 1

        print(colors.Red, end="")
        while chars_printed < length:
            sleep(.02)
            print("█", end="", flush=True)
            chars_printed += 1

        print(colors.Reset, end="")
