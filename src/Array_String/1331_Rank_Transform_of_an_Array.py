class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        temp = sorted([(num,i) for i,num in enumerate(arr)])
        rank = 0
        last = None
        for ele in temp:
            if last!= ele[0]:
                rank+=1
                last = ele[0]
            
            res[ele[1]] = rank
        
        return res
        
        