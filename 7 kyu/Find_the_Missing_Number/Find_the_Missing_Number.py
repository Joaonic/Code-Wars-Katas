def missing_no(nums):
    i, total = 0, 0
  
    for i in range(2, len(nums) + 2): 
        total += i 
        total -= nums[i - 2] 
    return total - 100