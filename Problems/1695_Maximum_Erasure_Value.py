class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # sliding window

        pt1 = 0
        pt2 = 0

        max_sum = 0
        cur_sum = 0

        window_dict = {}

        while pt2 < len(nums):
            if nums[pt2] not in window_dict or window_dict[nums[pt2]] == False:
                cur_sum += nums[pt2]
                max_sum = max(max_sum,cur_sum)
                window_dict[nums[pt2]] = True
            else:
                #print("deleteing")
                while True:
                    if nums[pt1] != nums[pt2]:
                        window_dict[nums[pt1]] = False
                        cur_sum -= nums[pt1]
                        pt1 += 1
                    else:
                        pt1 += 1
                        break
            pt2 += 1
            #print(pt1,pt2,window_dict,cur_sum)


        return max_sum

        