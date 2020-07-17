def solution(number):
    x = []
    for i in(range(number)):
        if i % 3 == 0:
            x.append(i)
        if i % 5 == 0:
            x.append(i)
    return sum(set(x))