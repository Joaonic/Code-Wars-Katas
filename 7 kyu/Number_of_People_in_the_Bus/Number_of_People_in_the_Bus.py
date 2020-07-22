def number(bus_stops):
    return sum([bus_stops[i][0] - bus_stops[i][1] for i in range(len(bus_stops))])
    # Good Luck!