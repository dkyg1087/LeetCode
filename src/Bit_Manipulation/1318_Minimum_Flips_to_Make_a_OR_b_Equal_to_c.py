class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        ans = 0

        while c != 0 or b != 0 or a != 0:
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1

            if a_bit | b_bit == c_bit:
                pass
            elif c_bit == 1:
                ans += 1
            else:
                if a_bit & b_bit != c_bit:
                    ans += 2
                else:
                    ans += 1

            a >>= 1
            b >>= 1
            c >>= 1
        
        return ans
            