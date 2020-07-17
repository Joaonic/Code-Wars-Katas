def friend(x):
    y = []
    for i in range(len(x)):
        if len(x[i]) == 4:
            y.append(x[i])
    return y