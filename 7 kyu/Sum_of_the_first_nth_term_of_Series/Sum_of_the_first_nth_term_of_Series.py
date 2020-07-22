def series_sum(n):
    return '{:.2f}'.format(sum([1/(1+i*3) for i in range(n)]))
    
    