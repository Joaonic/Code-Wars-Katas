def to_jaden_case(string):
    s = string.split()
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    return ' '.join(s)