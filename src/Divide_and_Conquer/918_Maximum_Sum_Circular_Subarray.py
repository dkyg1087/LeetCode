class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        # There's 2 situation, the max either crosses from end -> start or the normal way where it just like the normal one

        # If it is the normal way, we can find it normaly

        # If it is the other way, we find it by (total sum - the min sub array =  the largest none connecting sum)
        
        max_cur,min_cur,max_sum,min_sum,total_sum = 0,0,nums[0],nums[0],sum(nums)

        for num in nums:
            max_cur = max(max_cur + num,num)
            max_sum = max(max_sum,max_cur)

            min_cur = min(min_cur+num,num)
            min_sum = min(min_sum,min_cur)

        # If its full negative then we just return the max_sum

        if total_sum == min_sum:
            return max_sum
        
        return max(max_sum,total_sum-min_sum)