class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = math.ceil(sum(quantities) / n)
        right = max(quantities)

        while left < right:
            mid = left + (right - left) // 2
            store = sum([math.ceil(quant / mid) for quant in quantities])
            print(left,right,mid,store)
            if store <= n:
                right = mid
            else:
                left = mid + 1

        return left
            

        

        