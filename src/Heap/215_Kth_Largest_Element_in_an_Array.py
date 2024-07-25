class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Use counting sort and delete elements from the last
        # offset the negative numbers to make the min num to 0
        
        
        min_num = min(nums)
        max_num = max(nums)

        count = [0] * (max_num-min_num + 1)

        for num in nums:
            count[num - min_num] += 1
        
        remain = k

        for num in range(len(count) - 1,-1,-1):
            remain -= count[num]
            if remain <= 0:
                return num + min_num
        
        return -1

                        
            