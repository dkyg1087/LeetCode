class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def next(row:List):
            nextRow = []
            for a,b in zip(row[0:-1],row[1:]):
                nextRow.append(a+b)
            nextRow.append(1)
            nextRow.insert(0,1)
            return nextRow
        
        result = [[1]]
        
        for i in range(numRows-1):
            result.append(next(result[-1]))
    
        return result