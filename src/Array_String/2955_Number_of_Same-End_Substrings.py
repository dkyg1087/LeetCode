class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        prefix_sum = [[0] * 26 for _ in range(n)]
        
        for i, char in enumerate(s):
            char_index = ord(char) - ord('a')

            if i > 0:
                for j in range(26):
                    prefix_sum[i][j] = prefix_sum[i - 1][j]
            
            prefix_sum[i][char_index] += 1
        
        res = []
        
        for left_idx, right_idx in queries:
            temp_sum = 0

            for alph in range(26):
                left_freq = prefix_sum[left_idx-1][alph] if left_idx != 0 else 0
                right_freq = prefix_sum[right_idx][alph]
                diff = right_freq - left_freq
                if diff != 0 or diff != 1:
                    temp_sum += diff * (diff + 1) // 2

            res.append(temp_sum)
        
        return res
                    