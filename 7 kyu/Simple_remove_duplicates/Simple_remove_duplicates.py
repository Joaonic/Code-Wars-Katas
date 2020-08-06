def solve(arr): 
    return [arr[i] for i in range(len(arr)) if arr[i] not in arr[i+1:]]