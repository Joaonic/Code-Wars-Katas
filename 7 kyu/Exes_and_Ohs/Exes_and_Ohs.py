def xo(s):
    if list(s.lower()).count('x') == list(s.lower()).count('o') or (list(s.lower()).count('x') == 0 and list(s.lower()).count('o') == 0):
        return True
    else:
        return False