def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    else:
        for i in range(len(numbers)):
            if numbers[i] == min(numbers):
                return numbers[:i] + numbers[i+1:]
                break