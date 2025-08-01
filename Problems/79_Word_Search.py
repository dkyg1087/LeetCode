class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # backtracking through the actual list, change the visited ones into another char.
        # if it is a dead end, change it back to the original one.
        
        def backtrack(board,i,j,word,idx):
            if 0 > i  or i >= len(board) or 0 > j or j >= len(board[0]) or board[i][j] != word[idx]:
                return False
            
            if idx == len(word)-1:
                return True
            
            board[i][j] = "@"
            
            for dir_i,dir_j in [(1,0),(-1,0),(0,1),(0,-1)]:
                if backtrack(board,i+dir_i,j+dir_j,word,idx+1):
                    board[i][j] = word[idx]
                    return True
            
            board[i][j] = word[idx]
        
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(board,i,j,word,0):
                    return True
        
        return False
                    
