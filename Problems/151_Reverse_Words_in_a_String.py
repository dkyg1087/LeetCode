class Solution:
    def reverseWords(self, s: str) -> str:
        ans = deque([])
        s = s + " "
        SPACED = True
        temp = []
        for c in s:
            if c == " " and SPACED == False:
                SPACED = True
                ans.appendleft("".join(temp))
                temp = []
            elif c != " ":
                SPACED = False
                temp.append(c)

        return " ".join(ans)