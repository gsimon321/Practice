# Question 2: Stacks

# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, orIt can be written as AB (A concatenated with B), where A and B are valid strings, orIt can be written as (A), where A is a valid string.

# Example:

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opened = []
        stringList = list(s)
        
        for char in range(len(s)):
            if stringList[char] == "(":
                opened.append(char)
            elif stringList[char] == ")":
                if opened:
                    opened.pop()
                else:
                    stringList[char] = ""
                    
        for index in opened:
            stringList[index] = ""
        
        return "".join(stringList)



# testcase

string1 = "(asdn))"

string2 = "))))))()"
