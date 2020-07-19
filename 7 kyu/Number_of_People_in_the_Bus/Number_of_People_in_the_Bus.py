def number(bus_stops):
    ans = [bus_stops[i][0] - bus_stops[i][1] for i in range(len(bus_stops))]
    return sum(ans)
    # Good Luck!