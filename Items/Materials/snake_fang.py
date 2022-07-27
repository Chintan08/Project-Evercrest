from Utility.colors import colors

class snake_fang:

    sell = 8
    buy = None

    name = "Snake Fang"
    desc = f"{colors.LightCyan}A piece of a snake's fangs. It's still sharp!{colors.Reset}\n" \
           f"\n{colors.Green}BUY PRICE{colors.Reset}: {colors.Green}{buy}{colors.Reset}" \
           f"\n{colors.LightGreen}Sell Price: {colors.Green}${sell}{colors.Reset}"
    type = "material"
