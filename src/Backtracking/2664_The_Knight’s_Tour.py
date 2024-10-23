class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:

        board = [[-1 for _ in range(n)] for _ in range(m)]

        directions = ((2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2),(-1, 2),(-1, -2))
        def is_valid(i,j):
            nonlocal board
            return (
                0 <= i < len(board) and
                0 <= j < len(board[0]) and
                board[i][j] == -1 
            )

        def dfs(step,i,j):
            nonlocal directions
            nonlocal board
            board[i][j] = step
            if step == m*n -1:
                return True
            for delta_i,delta_j in directions:
                if is_valid(i+delta_i,j+delta_j):
                    if dfs(step + 1,i+delta_i,j+delta_j):
                        return True
            board[i][j] = -1

            return False
        dfs(0,r,c)
        return board
            

        

        
        