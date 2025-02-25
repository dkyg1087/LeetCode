class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix_sum = 0
        num_odd = 0
        num_even = 1
        ans = 0

        for num in arr:
            prefix_sum += num

            # if prefix is even
            if prefix_sum % 2 == 0:
                ans += num_odd
                num_even += 1
            else:
                ans += num_even
                num_odd += 1
            
            ans %= 10 ** 9 + 7
        
        return ans
                
