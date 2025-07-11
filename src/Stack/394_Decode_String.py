class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        
        for char in s:
            if char != "]":
                stk.append(char)
            else:
                tempStr = deque([])
                while stk[-1] != "[":
                    tempStr.appendleft(stk.pop())
                stk.pop()
                repeat = deque([])
                while len(stk) > 0 and stk[-1] in "0123456789":
                    repeat.appendleft(stk.pop())
                repeat = int("".join(repeat))

                tempStr = "".join(tempStr)
                tempStr *=  repeat
                stk.extend(tempStr)
            print(stk)

        return "".join(stk)