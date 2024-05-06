class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        validOperators = ["+", "-", "/", "*"]
        totalCurrentOperation = 0

        for token in tokens:
            if token not in validOperators:
                stack.append(token)
            else:
                secInt = int(stack.pop())
                firstInt = int(stack.pop())
                if token == validOperators[0] :
                    totalCurrentOperation = firstInt + secInt
                    stack.append(totalCurrentOperation)
                elif token == validOperators[1] :
                    totalCurrentOperation = firstInt - secInt
                    stack.append(totalCurrentOperation)
                elif token == validOperators[2] :
                    totalCurrentOperation = firstInt / secInt
                    stack.append(totalCurrentOperation)
                elif token == validOperators[3] :
                    totalCurrentOperation = firstInt * secInt
                    stack.append(totalCurrentOperation)
        return int(stack.pop())
                
    