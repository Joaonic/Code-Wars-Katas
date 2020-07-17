def capitalize(s):
    s = list(s)
    l = s
    k = s
    for i in range(len(s)):
        if i % 2 == 0:
            l[i] = s[i].capitalize()
    result = ''.join(l)
    for i in range(len(s)):
        if i % 2 == 0:
            s[i] = s[i].lower()
        if i % 2 != 0:
            k[i] = s[i].capitalize()
    result1 = ''.join(k)
    return [result, result1]