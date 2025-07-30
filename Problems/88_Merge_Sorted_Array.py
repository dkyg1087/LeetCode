class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        # Start from behind to save space

        ptr1,ptr2,ptr3 = m-1,n-1,len(nums1) - 1

        while ptr1 >= 0 or ptr2 >= 0:
            if ptr1 < 0:
                nums1[ptr3] = nums2[ptr2]
                ptr2 -= 1
                ptr3 -= 1
            elif ptr2 < 0:
                nums1[ptr3] = nums1[ptr1] 
                ptr1 -= 1
                ptr3 -= 1
            else:
                if nums1[ptr1] >= nums2[ptr2]:
                    nums1[ptr3] = nums1[ptr1]
                    ptr1 -= 1
                    ptr3 -= 1
                else:
                    nums1[ptr3] = nums2[ptr2] 
                    ptr2 -= 1
                    ptr3 -= 1
        
        return nums1