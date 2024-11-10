class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        pt1,pt2,pt3 = 0,0,0
        res = []

        while pt1 < len(arr1) and pt2 < len(arr2) and pt3 < len(arr3):
            if arr1[pt1] == arr2[pt2] == arr3[pt3]:
                res.append(arr1[pt1])
                pt1 += 1
                pt2 += 1
                pt3 += 1
            else:
                if arr1[pt1] < arr2[pt2]:
                    pt1 += 1
                elif arr2[pt2] < arr3[pt3]:
                    pt2 += 1
                else:
                    pt3 += 1
        
        return res

