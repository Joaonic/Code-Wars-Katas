def solve(st):    
    st = ''.join(sorted(st))  
    for i in range(1, len(st)):    
        if ord(st[i]) - ord(st[i - 1]) != 1:  
            return False
    return True