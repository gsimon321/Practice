class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = []
        precounter = 0
        for i in prices:
            diff.insert(precounter, 0)
            precounter += 1
        counterOut = 0
        for start in prices:
            print(start, " -- This is the start")
            counterInner = len(prices) - counterOut - 1
            for i in range(0,counterInner):
                if diff[counterOut] < (prices[i+counterOut+1] - start):
                    diff.insert(counterOut, prices[i+counterOut+1] - start)
                print(diff[counterOut])
            counterOut += 1
        return max(diff)