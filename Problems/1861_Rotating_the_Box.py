class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        res = [["."] * m for _ in range(n)]

        for i in range(m):
            last_available = (i,n-1)
            for j in range(n-1,-1,-1):
                if box[i][j] == ".":
                    pass
                elif box[i][j] == "*":
                    last_available = (i,j-1)
                    res[j][m-i-1] = "*"
                else:
                    res[last_available[1]][m - last_available[0] - 1] = "#"
                    last_available = (last_available[0],last_available[1]-1)

        return res
                    