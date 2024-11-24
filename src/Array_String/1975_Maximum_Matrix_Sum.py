class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum_max = 0
        abs_min = math.inf
        neg_count = 0

        for row in matrix:
            for num in row:
                if num < 0:
                    neg_count += 1

                sum_max += abs(num)
                abs_min = min(abs(num),abs_min)
        
        if neg_count % 2 != 0:
            return sum_max - abs_min - abs_min
        else:
            return sum_max 
            