class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newNums = []
        num = 0
        for i in nums: 
            newNum = 0
            if(num == 0):
                newNum = nums[0]
            else:
                print(num)
                dummyNum = num - 1 
                newNum = newNums[dummyNum] + nums[num]
            print(num)
            newNums.insert(num, newNum)
            num = num + 1 
        return newNums        
            

            