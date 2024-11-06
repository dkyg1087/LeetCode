class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        last_max = 0
        cur_max = nums[0]
        cur_bit = nums[0].bit_count() 

        for num in nums:
            cnt = num.bit_count()
            if cur_bit != cnt:
                cur_bit = cnt
                last_max = cur_max
                cur_max = 0
            cur_max = max(cur_max,num)
            
            if num < last_max:
                return False
    
        return True
