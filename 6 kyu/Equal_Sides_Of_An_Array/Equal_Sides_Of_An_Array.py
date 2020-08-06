def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
            break
    if i == len(arr) - 1:
        return -1
        
    #your code here