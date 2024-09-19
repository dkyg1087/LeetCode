class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        # Use the operators to split the left and right expressions to mimic a parentheses
        # Return all the possible answer for left and right expression
        # for each possibilty on the left, do the operation that we split on the right possiblities   

        def dfs(expression):
            oper = {
                "+":lambda x,y:x+y,
                "-":lambda x,y:x-y,
                "*":lambda x,y:x*y}
        
            res = []

            for i in range(len(expression)):
                if expression[i] in oper:
                    str1 = expression[:i]
                    str2 = expression[i+1:]

                    res1 = dfs(str1)
                    res2 = dfs(str2)

                    for j in res1:
                        for k in res2:
                            res.append(oper[expression[i]](j,k))
                
            if len(res) == 0:
                res.append(int(expression))
            
            return res
    
        return dfs(expression)



                
                
