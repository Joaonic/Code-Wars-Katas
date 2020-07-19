def find_next_square(sq):
    if sq ** 0.5 == int(sq ** 0.5):
        return (sq ** 0.5 + 1) ** 2
    else:
        return -1