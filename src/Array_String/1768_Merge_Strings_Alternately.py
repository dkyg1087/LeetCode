class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_len = len(word1)
        w2_len = len(word2)
        ans = ""
        for i in range(min(w1_len,w2_len)):
            ans += word1[i] + word2[i]
        
        if w1_len > w2_len:
            ans += word1[w2_len::]
        elif w1_len < w2_len:
            ans += word2[w1_len::]
        
        return ans