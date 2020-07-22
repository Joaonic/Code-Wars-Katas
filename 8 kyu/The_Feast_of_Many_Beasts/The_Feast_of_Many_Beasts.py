def feast(beast, dish):
    if beast[0] == dish[0] and beast[len(beast)-1] == dish[len(dish)-1]:
        return True
    else:
        return False