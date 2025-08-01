class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_dict = {}
        row_dict = {}
        grid_dict = {}

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    pass
                else:
                    if i not in row_dict:
                        row_dict[i] = set()
                    else:
                        if board[i][j] in row_dict[i]:
                            return False
                    
                    if j not in col_dict:
                        col_dict[j] = set()
                    else:
                        if board[i][j] in col_dict[j]:
                            return False
                    
                    if (i//3,j//3) not in grid_dict:
                        grid_dict[(i//3,j//3)] = set()
                    else:
                        if board[i][j] in grid_dict[(i//3,j//3)]:
                            return False
                    
                    col_dict[j].add(board[i][j])
                    row_dict[i].add(board[i][j])
                    grid_dict[(i//3,j//3)].add(board[i][j])
        return True