class Solution:
    def isValid(self, s: str) -> bool:

        # Create a stack to store parentheses, if we encounter a closing one then we chaeck the last one we stored to see if it matches

        stack = []
        for char in s:
            if not stack:

                # If we simply start with a ending one then its invalid for sure and we early stop

                if char in (')',']','}'):
                    return False
                stack.append(char)
            else:
                if char in ('(','[','{'):
                    stack.append(char)
                else:

                    # If we encounter a closing one we check if the last one is the correct opening one, if yes we pop the open one and if not we return False

                    if char == ')':
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            return False
                    elif char == ']':
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            return False
                    else:
                        if stack[-1] == '{':
                            stack.pop()
                        else:
                            return False
        if stack:
            return False
        
        return True
                

                