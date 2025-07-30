class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        length = len(word)
        cur_max = -1
        ans = ""
        
        for i in range(len(word)):
            if ord(word[i]) - ord('a') >= cur_max:
                temp_word = ""
                if i < numFriends-1:
                    tmp_word = word[i:length-(numFriends-1-i)]
                else:
                    tmp_word = word[i:length]
                ans = max(ans,tmp_word)
        
        return ans