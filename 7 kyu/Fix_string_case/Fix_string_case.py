def solve(s):
    cont = 0
    for string in list(s):
        if string.isupper():
            cont += 1
    if cont > len(s)/2:
        return s.upper()
    else:
        return s.lower()