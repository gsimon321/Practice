class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        totalPalindrome = 0
        odd = 0
        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
                
        for char in letters:
            if letters[char] > 1:
                if letters[char] % 2 == 0:
                    totalPalindrome += letters[char]
                else:
                    totalPalindrome += letters[char] - 1
                    odd += 1
            else:
                odd += 1
                
        if odd > 0:
            totalPalindrome += 1
                
        return totalPalindrome