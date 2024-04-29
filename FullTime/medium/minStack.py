class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(self.minStack[len(self.minStack) - 1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
       self.minStack[len(self.minStack) - 1]