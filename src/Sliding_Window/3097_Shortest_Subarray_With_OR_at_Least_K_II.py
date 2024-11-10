class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        def add_to_current(bits,number,delta):
            i = 0
            while number > 0:
                if number & 1 == 1:
                    bits[i] += delta
                i += 1
                number >>= 1
        
        def bits_to_number(bits):
            res = 0
            for i in range(32):
                if bits[i]:
                    res |= 1 << i
            return res
                
        bits = [0] * 32

        min_length = math.inf

        start,end = 0,0

        while end < len(nums):
            add_to_current(bits,nums[end],1)

            while start <= end and bits_to_number(bits) >= k:
                min_length = min(min_length,end - start + 1)

                add_to_current(bits,nums[start],-1)
                start += 1
            
            end += 1
        
        return min_length if min_length != math.inf else -1
            

        