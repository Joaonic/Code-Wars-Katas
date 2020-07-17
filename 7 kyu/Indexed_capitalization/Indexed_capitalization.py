def capitalize(s,ind):
    s = ''.join(c if i in(ind) else c.upper() for i,c in enumerate(s))
    return s.swapcase()
    