def digital_root(n):
    for j in range(len(str(n))):
        n = sum([int(i) for i in list(str(n))])
    return n

    