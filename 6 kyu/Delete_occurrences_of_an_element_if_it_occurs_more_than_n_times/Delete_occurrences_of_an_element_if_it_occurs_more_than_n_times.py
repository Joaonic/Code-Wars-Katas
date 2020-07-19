def delete_nth(lst, n):
    result = []
    for number in lst:
        if result.count(number) < n:
            result.append(number)
    return result