class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        direction = ((0,1),(1,0),(0,-1),(-1,0))
        i,j,k = 0,0,0
        for _ in range(len(matrix)*len(matrix[0])):
            if matrix[i][j] != 'a':
                output.append(matrix[i][j])
                matrix[i][j] = 'a'
            
            if not (0 <= i + direction[k][0] < len(matrix)) or not (0 <= j + direction[k][1] < len(matrix[0])) or matrix[i+direction[k][0]][j+direction[k][1]] == 'a':
                k += 1
                k %= 4
 
            i += direction[k][0]
            j += direction[k][1]
        
        return output