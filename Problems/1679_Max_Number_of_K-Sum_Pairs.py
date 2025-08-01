class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        table = defaultdict(int)
        for n in nums:
            if table[k - n] != 0:
                ans += 1
                table[k-n] -= 1
            else:
                table[n] += 1
        
        return ans