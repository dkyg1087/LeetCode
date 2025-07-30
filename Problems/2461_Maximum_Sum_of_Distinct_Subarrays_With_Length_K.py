class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sum_cur = nums[0]
        max_res = 0
        window_dict = {nums[0]:1}

        l,r = 0,0

        while r < len(nums):
            #print(l,r,r-l,len(window_dict))
            if r - l + 1 == k:
                if len(window_dict) == k:
                    max_res = max(sum_cur,max_res)
                if window_dict[nums[l]] != 1:
                    window_dict[nums[l]] -= 1
                else:
                    del window_dict[nums[l]]
                sum_cur -= nums[l]
                l += 1
            else:
                r += 1
                if r < len(nums):
                    sum_cur += nums[r]
                    if nums[r] not in window_dict:
                        window_dict[nums[r]] = 1
                    else:
                        window_dict[nums[r]] += 1
                
        return max_res 


            
            
        
        