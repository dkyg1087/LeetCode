class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        idx1,idx2 = 0,0
        ans = []
        while idx1 < len(nums1) or idx2 < len(nums2):
            if idx1 == len(nums1):
                ans.append(nums2[idx2])
                idx2 += 1
            elif idx2 == len(nums2):
                ans.append(nums1[idx1])
                idx1 += 1
            else:
                if nums1[idx1][0] > nums2[idx2][0]:
                    ans.append(nums2[idx2])
                    idx2 += 1
                elif nums1[idx1][0] < nums2[idx2][0]:
                    ans.append(nums1[idx1])
                    idx1 += 1
                else:
                    ans.append([nums2[idx2][0],nums1[idx1][1] + nums2[idx2][1]])
                    idx1 += 1
                    idx2 += 1
                
        return ans
            