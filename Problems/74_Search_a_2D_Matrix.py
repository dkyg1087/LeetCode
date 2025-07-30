class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def one_d_to_two_d(idx,matrix):
            return idx // len(matrix[0]), idx % len(matrix[0])
        

        matrix_len = len(matrix) * len(matrix[0])
        def binary_search(left,right,targ):
            if left > right:
                return False
            mid = (left + right) // 2
            i,j = one_d_to_two_d(mid,matrix)
            if matrix[i][j] == targ:
                return True
            elif matrix[i][j] > targ:
                return binary_search(left,mid-1,targ)
            elif matrix[i][j] < targ:
                return binary_search(mid+1,right,targ)
        
        return binary_search(0,matrix_len - 1,target)
            
                
                
        
