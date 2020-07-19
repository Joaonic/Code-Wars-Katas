def iq_test(numbers):
    numbers = numbers.split()
    evens = []
    odds = []
    for number in numbers:
        if int(number) % 2 == 0:
            evens.append(number)
        if int(number) % 2 != 0:
            odds.append(number)
    if len(odds) == 1:
        return numbers.index(odds[0]) + 1
    if len(evens) == 1:
        return numbers.index(evens[0]) + 1