class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lt = []
        gt = []
        piv = []

        for n in nums:
            if n < pivot:
                lt.append(n)
            elif n > pivot:
                gt.append(n)
            else:
                piv.append(n)
        
        nums[:len(lt)] = lt[::]
        nums[len(lt):len(lt)+len(piv)] = piv[::]
        nums[len(lt)+len(piv):len(lt)+len(piv)+len(gt)] = gt[::]
        return nums
            