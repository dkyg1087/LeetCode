class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        word_count = defaultdict(int)
        double_count = 0
        for word in words:
            rev = word[::-1]
            if word[0] == word[1]:
                double_count += 1
            
            if rev in word_count and word_count[rev] > 0:
                if rev == word:
                    double_count -= 2
                word_count[rev] -= 1
                ans += 4
            else:
                word_count[word] += 1
        return ans+2 if double_count > 0 else ans 