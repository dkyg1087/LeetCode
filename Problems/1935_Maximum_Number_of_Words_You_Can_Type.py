class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        if len(text) == 0:
            return 0
        broken_counter = Counter(brokenLetters)
        words = text.split(" ")
        ans = len(words)
        for word in words:
            for c in word:
                if c in broken_counter:
                    ans -= 1
                    break
        
        return ans
