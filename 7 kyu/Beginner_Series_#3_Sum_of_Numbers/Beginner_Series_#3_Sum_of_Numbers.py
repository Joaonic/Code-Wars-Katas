def get_sum(a,b):
    x = []
    if a == b:
        return a
    if a < b:
        return a + get_sum(a+1, b)
    else:
        return a + get_sum(a-1, b)