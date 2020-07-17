def waterbombs(fire, w):
    cont = 0
    result = 0
    def split(word): 
        return [char for char in word]   
    fire = split(fire)
    for i in range(len(fire)):
        if fire[i] == 'x':
            cont += 1
        if cont == w:
            cont = 0
            result += 1
        if fire[i] == 'Y' and 0 < cont <= w:
            cont = 0
            result += 1 
    if 0 < cont <= w:
        result +=1
    if cont > w:
        prod = cont/w
        if prod % int(prod) != 0:    
            result += int(prod) + 1
        else:
            result += int(prod)
    return result