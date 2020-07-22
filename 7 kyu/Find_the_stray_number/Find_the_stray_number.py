def stray(arr):
    return [n for n in arr if arr.count(n) == 1][0]