def is_square(n):
    if n > 0 and (n ** 0.5) % int(n ** 0.5) == 0 or n == 0:
        return True
    else:
        return False