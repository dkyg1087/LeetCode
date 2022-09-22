#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sett = set()
        for i in range(9):
            for j in range(9):
                c = str(board[i][j])
                if c == ".":
                    continue
                if c+"row"+str(i) in sett or c+"col"+str(j) in sett or c+"row"+str(i//3)+"col"+str(j//3) in sett:
                    return False
                else:
                    sett.add(c+"row"+str(i))
                    sett.add(c+"col"+str(j))
                    sett.add(c+"row"+str(i//3)+"col"+str(j//3))
        return True
# @lc code=end

