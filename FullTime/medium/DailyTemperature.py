class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # brute force would just be do a double forloop and count through, O(n^2)

        # instead we should do something where we make use of a stack but go from the back
        # the last value is always gonna be 0
        res = [0] * len(temperatures)
        stack = [] # this is going to be a tuple stack with value + index

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t,i])

        return res