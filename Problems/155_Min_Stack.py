class MinStack:

    # We maintain 2 stacks, one actual stack and one min stack
    # As we push elements into the stack, we store the current min in the min stack.
    # Meaning that until this element gets poped in the actual stack, this stack's min element is this one.
    # We make it a stack because we need to know what were the min before the current min so that we can know after the current min is poped. 



    def __init__(self):
        self.stack = []
        self.minStack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()