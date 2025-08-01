class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parents = {}
    
        for alpha in ascii_lowercase:
            parents[alpha] = alpha
            

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(a,b):
            aroot = find(a)
            broot = find(b)
            if aroot == broot:
                return

            if aroot < broot:
                parents[broot] = aroot
            else:
                parents[aroot] = broot


        for a,b in zip(s1,s2):
            union(a,b)
                
        ans = []
        
        for w in baseStr:
            ans.append(find(w))
        
        return "".join(ans)

