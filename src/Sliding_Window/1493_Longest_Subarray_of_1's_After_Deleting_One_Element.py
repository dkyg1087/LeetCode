class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        wl,wr = 0,0
        max_length = 0
        while wr < len(nums):

            if nums[wr] == 0:
                zero_count += 1
            
            if zero_count <= 1:
                max_length = max(max_length,wr - wl + 1)

            while zero_count > 1:
                if nums[wl] == 0:
                    zero_count -= 1
                wl += 1
            
            wr += 1

        return max_length - 1