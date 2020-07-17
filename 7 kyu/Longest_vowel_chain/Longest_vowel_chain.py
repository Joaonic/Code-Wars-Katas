def solve(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    cont = 0
    cont1 = 0
    s = list(s)
    for i in range(len(s)):
        if s[i] in vowels:
            cont += 1
        elif s[i] is not vowels:
            if cont > cont1: cont1 = cont
            cont = 0
    return cont1