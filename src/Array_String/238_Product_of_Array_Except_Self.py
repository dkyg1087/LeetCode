class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = 1, 1
        ptr1 , ptr2 = 0, len(nums) -1
        ans = [1] * len(nums)
        while ptr1 < len(nums):
            ans[ptr1] *= prefix
            ans[ptr2] *= suffix

            prefix *= nums[ptr1]
            suffix *= nums[ptr2]

            ptr1 += 1
            ptr2 -= 1
        
        return ans
            