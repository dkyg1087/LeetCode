class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # treat the list as "can the string be contructed using the word dict so far."
        # update each accordingly to check if the word fits in or not
        # check if you can fit in the current word as well as if the string before the current word is valid/
        
        
        dp = [False] * len(s)


        for i in range(len(s)):
            for word in wordDict:
                if i + 1 - len(word) < 0:
                    continue
                
                if i == len(word) -1 or dp[i-len(word)]:
                    if s[i-len(word)+1:i+1] == word:
                        dp[i] = True
                        break
        return dp[-1]