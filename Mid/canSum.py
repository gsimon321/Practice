# is there a sub set that sums to a given value
# all numbers are non negative

# if target is 9 and set is {1,3,5,4,33,55}
# then the numbers 5 and 4 will sum to 9 for example.
# We can also rule out some the numbers here if they are too large
# so 33 and 55 can go for example

def canSum(nums, target):
    if target == 0:
        return True
    if (target < 0):
        return False
    for i in range(len(nums)):
        remainder = target - nums[i]
        if canSum(nums,remainder) == True:
            return True

    return False

print(canSum([5,3], 7))
    
        
    
    
