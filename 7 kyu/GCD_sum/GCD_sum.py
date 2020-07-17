def solve(sum,n2):
    def gcd(x, y):
        gcd = 1
        divisor  = 2 
        while divisor <= x:
            if x % divisor == 0 and y % divisor == 0:
                gcd = divisor
            divisor += 1
        if gcd <= 1:
            return -1
        else:
            return gcd
    # sum != gcd checks that both the 
    # numbers are positive or not 
    if (gcd(n2, sum - n2) == n2 and
                          sum != n2): 
        return(min(n2, sum - n2),  
               sum - min(n2, sum - n2)) 
    else: 
        return -1 