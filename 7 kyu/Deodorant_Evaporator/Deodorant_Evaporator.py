def evaporator(content, evap_per_day, threshold):
    n_days = 0
    content1 = content
    while content1 >= (content * threshold / 100):
        content1 -= content1*evap_per_day/100
        n_days += 1
    return n_days