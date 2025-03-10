class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        wr = 0
        window_sum = 0
        max_sum = -1 * math.inf
        while wr < len(nums):
            window_sum += nums[wr]
            if wr + 1 - k >= 0:
                max_sum = max(max_sum,window_sum)
                window_sum -= nums[wr + 1 - k]
            wr += 1
            
        return max_sum / k