def remove_char(s):
    s =  list(s)
    del(s[0])
    del(s[len(s)-1])
    s = ''.join(s)
    return s