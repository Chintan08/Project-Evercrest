from time import sleep

class dialogue:

    @staticmethod
    def dia(suffix, string):
        #stime = 0
        index = len(string)

        if suffix is not None:
            print(f"{suffix}:")
        else:
            print("")

        while index != 0:
            sleep(.02)
            print(string[len(string)-index], end="", flush=True)
            #stime+=.01
            index -= 1
        print("\n")
        sleep(1)
        #sleep(stime)