class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # rotate 90 = transpose -> horizontal mirror 
        # rotate 180 = rotate 90 -> rotate 90
        # rotate 270 = horizontal mirror -> transpose

        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1] = matrix[i][n-j-1],matrix[i][j]
