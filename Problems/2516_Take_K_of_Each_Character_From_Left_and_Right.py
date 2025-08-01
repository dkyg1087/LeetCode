class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = [0] * 3

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
        
        if not all([count[i] >= k for i in range(3)]):
            return -1
        
        window = [0] * 3

        left,max_window = 0, 0

        for right in range(len(s)):
            window[ord(s[right]) - ord('a')] += 1
            
            while left <= right and any([(count[i] - window[i]) < k for i in range(3)]):
                window[ord(s[left]) - ord('a')] -= 1
                left += 1
            
            max_window = max(max_window,right - left + 1)
        
        return len(s) - max_window
        