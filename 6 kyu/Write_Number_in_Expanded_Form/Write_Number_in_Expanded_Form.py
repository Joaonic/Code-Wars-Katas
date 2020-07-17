def expanded_form(num):
    a =[]
    number = num
    while number != 0:
        number, rem = divmod(number, 10)
        a.append(rem)
    a.reverse()

    b = []
    counter = len(a)
    for n in a:
        b.append(n*(10**(counter-1)))
        counter-=1


    return ' + '.join([str(num) for num in b if num != 0])