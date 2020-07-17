def find_short(s):
    a = []
    s = s.split()
    for i in range(len(s)):
        a.append(len(s[i]))
        b = min(a)
    return b # l: shortest word length