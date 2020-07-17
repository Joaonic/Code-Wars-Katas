def open_or_senior(data):
    x = []
    data = list(data)
    for i in range(len(data)):
        if data[i][0] >= 55:
            if data[i][1] > 7:
                x.append('Senior')
            else:
                x.append('Open')
        else:
            x.append('Open')
    return x