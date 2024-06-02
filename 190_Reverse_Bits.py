class Solution:
    def reverseBits(self, n: int) -> int:
        
        # reverse bits one bit at a time by & with 1 and combine it with |

        res = 0

        for i in range(32):

            # consider 000001 & 1010101 -> we will only get the least significant bit

            num = n & 1

            # Shift n one bit to the right

            n = n >> 1

            # Shift res one bit to the left

            res = res << 1

            # consider 000001 | 111110 -> 1111111 combine the least bit to the res

            res = res | num
        
        return res