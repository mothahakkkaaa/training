def make_negative( number ):
    if number > 0:
        return -number
    elif number < 0:
        return number
    elif number == 0:
        return 0


figure = 0
print(make_negative(figure))