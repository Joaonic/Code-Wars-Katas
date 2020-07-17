def printer_error(s):
    x = 0
    s = list(s)
    test = list('nopqrstuvwxyz')
    for i in range(len(test)):
        x = x + s.count(test[i])
    x = str(x)
    y = str(len(s))
    return x + '/' + y