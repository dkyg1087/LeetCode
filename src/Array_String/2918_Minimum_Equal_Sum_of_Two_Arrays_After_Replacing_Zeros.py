class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        z1 = nums1.count(0)
        z2 = nums2.count(0)

        n1 = sum(nums1)
        n2 = sum(nums2)

        if n2 + z2 > n1 + z1:
            n1, n2 = n2, n1
            z1, z2 = z2, z1
        
        targ = n1 + z1
        
        if (targ - n2 >= z2 and z2 != 0) or targ == n2 and z2 == 0:
            return targ
        else:
            return -1

        
            

