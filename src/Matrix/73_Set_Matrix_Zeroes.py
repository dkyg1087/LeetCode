class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # Use the first row and col as the indicator of whether this row/col needs to be 0 or not
        # for checking the first row and col, we use [0][0] for the row and asign another variable 'col' to indicate

        m,n = len(matrix),len(matrix[0])
        col = False
        for i in range(m):

            if matrix[i][0] == 0:
                col = True

            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        
        if col:
            for i in range(m):
                matrix[i][0] = 0
        return 