def square_digits(num):
    return int(''.join([str(int(n) ** 2) for n in list(str(num))]))