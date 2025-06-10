class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0

        cols = defaultdict(int)
        rows = defaultdict(int)

        for i in range(len(grid)):
            a = tuple(grid[i]) # row
            b = tuple(row[i] for row in grid) # col
            if a in cols:
                ans += cols[a]
            rows[a] += 1

            if b in rows:
                ans += rows[b]
            cols[b] += 1

        return ans

                