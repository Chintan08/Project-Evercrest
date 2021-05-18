from time import sleep
from colored import fore, style
from Utility.colors import colors

def gen_menu_enum(greet, options, inp, sleep_time):

    print(f"\n{colors.LightCyan}{greet}{colors.Reset}\n\n")

    print("\n".join([f"{index + 1}. {item}" for index, item in enumerate(options)]))

    while True:
        try:
            ans = int(input(f"\n\n{colors.LightCyan}{inp}{colors.Reset}\n"))

            if ans not in range(1, len(options)+1):
                raise ValueError

            return ans

        except ValueError:
            print(f"\n{fore.RED}That's not an option.{style.RESET}\n")


# creates a menu when called upon
def gen_menu_num(greet, options, inp, sleep_time):

    option = 0
    while True:
        print(f"\n{colors.LightCyan}{greet}{colors.Reset}\n\n")

        for index in range(0, len(options)):
            sleep(sleep_time)

            if len(options[index]) <= 0:
                pass
            else:
                print(f"{index + 1}. {options[index]}")
                option+=1

        try:
            ans = int(input(f"\n\n{colors.LightCyan}{inp}{colors.Reset}\n"))

            if ans not in range(1, option+1):
                raise ValueError

            return ans

        except ValueError:
            print(f"\n{fore.RED}That's not an option.{style.RESET}\n")


# returns a 1 if yes, returns 0 if no
def gen_menu_yn(inp):
    while True:
        ans = input(f"{colors.LightCyan}{inp}{colors.Reset} ({colors.LightGreen}Y{colors.White}/{colors.LightRed}N{colors.Reset})\n")

        if ans.lower() == "y":
            return 1

        elif ans.lower() == "n":
            return 0

        else:
            print(f"{fore.RED}\nThat's not an option.{style.RESET}")
