class Solution:
    def climbStairs(self, n: int) -> int:
        
        # The current step = the last step with 1 step + the step before with 2 steps
        # e.g. fib seq
        
        ways = 0
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        first,seccond = 1,2

        for _ in range(n-2):
            ways = first + seccond
            first = seccond
            seccond = ways

        return ways  