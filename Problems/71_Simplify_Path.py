class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # A function to find the next '/' and return what ever is between them
        
        def parsePath(path:str) -> str:
            idx = 1

            while idx < len(path):
                temp = ''
                while idx < len(path) and path[idx] != '/':
                    temp += path[idx]
                    idx += 1
                idx += 1
                yield temp
        
        # Use a stack to store the directory names

        stack = []
        
        for s in parsePath(path):

            # if it's ".." we pop the last directory bc it means to go up by 1

            if s == "..":
                if stack:
                    stack.pop()

            # If it's nothing or "." means there's multiple slashes or a single dot meaning current directory so we ignore them 

            elif s in ("","."):
                continue
            
            # If anything else comes in we treat it as a directory and we add it to the stack

            else:
                stack.append(s)

        res = "/"
        for p in stack:
            res += str(p) + "/"
        
        return res[:-1:] if res != "/" else res
        


            
            
