def wave(people):
    return [people[:i].lower() + people[i:].capitalize() for i in range(len(people)) if (people[:i].lower() + people[i:].capitalize()).islower() == False]