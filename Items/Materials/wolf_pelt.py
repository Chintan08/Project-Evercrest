from Utility.colors import colors

class wolf_pelt:

    sell = 10
    buy = None

    name = "Wolf Pelt"
    desc = f"{colors.LightCyan}A nice pelt taken from a Wolf.{colors.Reset}\n" \
           f"\n{colors.Green}BUY PRICE{colors.Reset}: {colors.Green}{buy}{colors.Reset}" \
           f"\n{colors.LightGreen}Sell Price: {colors.Green}${sell}{colors.Reset}"
    type = "material"
