def row_sum_odd_numbers(n):
    if n == 1:
        return 1
    x = (n-1) * n - 1
    y = []
    for i in range(n):
        x += 2
        y.append(x)
    x = 0
    for i in range(len(y)):
        x += y[i]
    return x