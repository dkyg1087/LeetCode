class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # We brute force the addition but we reverse the two bit strings because it would make it easier to calculate.
        # after we reverse it we reverse the final result.

        a_b,b_b,carry = 0,0,0

        digit = 0

        res = ""

        a_r,b_r = a[::-1],b[::-1]

        while True:
            
            if carry == 0 and digit >= len(a_r) and digit >= len(b_r):
                break

            a_b = int(a_r[digit]) if len(a_r) > digit else 0
            b_b = int(b_r[digit]) if len(b_r) > digit else 0
            
            temp = a_b + b_b + carry

            if temp == 0:
                res += "0"
            elif temp == 1:
                res += "1"
                carry = 0
            elif temp == 2:
                res += "0"
                carry = 1
            else:
                res += "1"
                carry = 1
            
            digit += 1
        
        return res[::-1]
