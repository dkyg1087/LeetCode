class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # step in one everytime a new number is chosen
        # to make it combination just don't iterate through the old numbers(e.g. the ones before the last number)
        
        output = []

        def create_combi(output,n,k,cur):
            if len(cur) == k:
                output.extend([cur[1:] + [i] for i in range(cur[-1]+1,n+1)])
                return
            for i in range(cur[-1]+1,n+1):
                create_combi(output,n,k,cur+[i])
        
        create_combi(output,n,k,[0])
        return output
        