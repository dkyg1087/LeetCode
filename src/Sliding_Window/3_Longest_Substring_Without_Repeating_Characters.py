class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Sliding window, store the char's next index so that everytime we see duplicate char, we can jump straight to the next one
        
        
        left,right = 0,0
        ans = 0

        index_char_next = {}

        while right < len(s):
            if s[right] in index_char_next:
                left = max(index_char_next[s[right]],left)
            
            ans = max(right - left + 1, ans)
            index_char_next[s[right]] = right + 1
            right += 1
        
        return ans

            
            
            
            