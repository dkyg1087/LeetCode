class Solution:
    def mySqrt(self, x: int) -> int:
        
        # Use binary search
        
        if x < 4:
            return 1 if x else 0
        
        lower,higher,temp = 2, x, -1 

        while lower <= higher:
            temp = (lower + higher) // 2

            if temp ** 2 == x:
                return temp
            elif temp ** 2 > x:
                higher = temp - 1
            else:
                lower = temp + 1

        return  temp - 1 if temp ** 2 > x else temp
            