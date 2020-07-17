def persistence(n):
    n = list(str(n))
    def cont(n, number, cont1):
        for i in n:
            number *= int(i)
        if len(list(str(number))) != 1:
            cont1 += 1
            cont1 = cont(list(str(number)), 1, cont1)
        return cont1
    if len(n) > 1:
        return cont(n, 1, 0) + 1
    else:
        return 0