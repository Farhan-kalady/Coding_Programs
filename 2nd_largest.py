nums = [80, 41, 20, 90, 45, 60]
largest = float("-inf")
s_largest = float("-inf")
n = len(nums) 
for i in range(0, n):
    if nums[i] > largest:
        s_largest = largest
        largest = nums[i]
    elif nums[i] > s_largest and nums[i] != largest:
        s_largest = nums[i]  
        
print(s_largest)              
     