class Solution:
    def countBits(self, n: int) -> List[int]:
        idx = 0
        ans = [0]
        reset = 0
        for _ in range(n):
            ans.append(ans[idx] + 1)
            if idx == reset:
                idx = 0
                reset = len(ans) - 1
            else:
                idx += 1

        return ans
            
