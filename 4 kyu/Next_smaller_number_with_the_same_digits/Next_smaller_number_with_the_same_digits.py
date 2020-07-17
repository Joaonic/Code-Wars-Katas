def next_smaller(number):
    new_number = number
    digit = list(str(number))  
    digits = len(digit)-1
    for index_1 in range(digits-1, -1, -1): 
        for index_2 in range(digits, index_1-1, -1): 
            if digit[index_2] < digit[index_1]:
                digit[index_2], digit[index_1] = digit[index_1], digit[index_2]
                _first = digit[0:index_1+1]
                _second = digit[-1:index_1:-1] 
                digit = _first + _second
                new_number = int(''.join(digit))
                if digit[0] == '0':
                    return -1
                return new_number
    if new_number == number:
        return -1
    return new_number