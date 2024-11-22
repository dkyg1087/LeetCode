class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = {}
        res = 0
        
        for row in matrix:
            rpr = 0
            for num in row:
                rpr <<= 1
                rpr |= num
            invert = ~rpr & ((1 << len(row)) - 1)
            rpr = rpr if rpr < invert else invert
            if rpr in count:
                count[rpr] += 1
            else:
                count[rpr] = 1
            res = max(count[rpr],res)
        
        return res
