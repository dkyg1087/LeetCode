class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 2 -> 1 change to 0 next stage
        # -1 -> 0 change to 1 next stage

        def check_survive(board,i,j):
            directions = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]

            alive = 0
            for x,y in directions:
                if 0 <= i+x < len(board) and 0 <= j+y < len(board[0]):
                    if board[i+x][j+y] > 0:
                        alive += 1

            if (board[i][j] == 0 and alive == 3) or (board[i][j] == 1 and alive in (2,3)):
                return True
            else:
                return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if check_survive(board,i,j):
                    if board[i][j] == 0:
                        board[i][j] = -1
                else:
                    if board[i][j] == 1:
                        board[i][j] = 2
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 0
                if board[i][j] == -1:
                    board[i][j] = 1