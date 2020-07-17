def high_and_low(numbers):
    numbers = numbers.split()
    numbers = [int(val) for val in numbers]
    return str(max(numbers)) + ' ' + str(min(numbers))