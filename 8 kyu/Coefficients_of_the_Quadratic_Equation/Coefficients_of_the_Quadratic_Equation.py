def quadratic(x1, x2):
    if x1 != 0: return (1, (x1 * -1) + (x2 * -1), x1 * x2)
    else:
        return (1, -1 * x2, x1*x2)