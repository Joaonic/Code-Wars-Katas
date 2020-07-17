def rgb(r, g, b):
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))
    return "{:02x}{:02x}{:02x}".format(r,g,b).upper()