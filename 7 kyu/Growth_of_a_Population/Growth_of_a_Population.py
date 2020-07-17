def nb_year(p0, percent, aug, p):
    cont = 0
    while p0 < p:
        p0 = p0 * (1 + percent / 100) + aug
        cont += 1
    return cont