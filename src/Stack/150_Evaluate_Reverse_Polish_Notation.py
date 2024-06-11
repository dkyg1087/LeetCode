class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # Literly just use a stack, if we encounter a symbol we do the correct operation and push the result back into the stack.
        
        stack = []
        
        for token in tokens:
            
            if token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(str(int(a)*int(b)))
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(str(int(int(b)/int(a))))
            elif token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(str(int(a)+int(b)))
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(str(int(b)-int(a)))
            else:
                stack.append(token)
            
        return int(stack.pop())
        