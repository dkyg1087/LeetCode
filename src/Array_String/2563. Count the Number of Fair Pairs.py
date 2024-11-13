class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        # sum of the two between lower and upper = sum of the two less than upper + 1 - sum of the two less than lower

        def find_amount(nums,targ):
            res = 0
            left = 0
            right = len(nums) - 1

            while left < right:
                sum = nums[left] + nums[right]

                if sum < targ:
                    res += right - left
                    left += 1
                else:
                    right -= 1
            
            return res
        

        return find_amount(nums,upper+1) - find_amount(nums,lower)
            
