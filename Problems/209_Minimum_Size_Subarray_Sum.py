class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start,end = 0,0
        cur_sum = nums[0]
        global_min = len(nums) + 10
        
        while start < len(nums):
            if cur_sum < target and end < len(nums) - 1:
                end += 1
                cur_sum += nums[end]
            elif cur_sum < target and end == len(nums) - 1:
                break
            elif cur_sum >= target:
                global_min = min(global_min,end - start + 1)
                if start < len(nums) - 1:
                    cur_sum -= nums[start]
                    start += 1
                else:
                    break
                

                
        
        return global_min if global_min != len(nums) + 10 else 0
                
                
             

         