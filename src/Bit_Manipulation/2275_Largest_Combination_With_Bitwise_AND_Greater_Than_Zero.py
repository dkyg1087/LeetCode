class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_length = math.ceil(math.log(10**7,2))
        ans = 0
        
        for i in range(bit_length):
            cur_sum = 0
            for j in range(len(candidates)):
                if candidates[j] & (1 << i) != 0:
                    cur_sum += 1
            ans = max(ans,cur_sum)
        
        return ans