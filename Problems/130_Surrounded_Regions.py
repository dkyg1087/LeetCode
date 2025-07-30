class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # Go around the edge to find any safe circles
        # Mark it safe
        # iterate through the matrix, mark not safe all "X" and safe ones "O"

        def mark_safe(board,i,j):
            stk = [(i,j)]
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            m = len(board)
            n = len(board[0])
            while len(stk) != 0:
                cur_i,cur_j = stk.pop()
                board[cur_i][cur_j] = "S"
                for dir_i,dir_j in directions:
                    if 0 <= cur_i+dir_i < m and 0 <= cur_j+dir_j < n and board[cur_i+dir_i][cur_j+dir_j] == "O":
                        stk.append((cur_i+dir_i,cur_j+dir_j))
        m = len(board)
        n = len(board[0])
        for i in range(m):
            if board[i][0] == "O":
                mark_safe(board,i,0)
            if board[i][-1] == "O":
                mark_safe(board,i,n-1)
        for i in range(len(board[0])):
            if board[0][i] == "O":
                mark_safe(board,0,i)
            if board[-1][i] == "O":
                mark_safe(board,m-1,i)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "S":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"


