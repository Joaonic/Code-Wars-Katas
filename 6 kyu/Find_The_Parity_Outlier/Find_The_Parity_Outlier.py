def find_outlier(a):
    x = []
    y = []
    for i in range(len(a)):
        if a[i] % 2 != 0:
            x.append(a[i])
        if a[i] % 2 == 0:
            y.append(a[i])
    if len(y) > len(x):
        x = x[0]
        return x
    else:
        y = y[0]
        return y