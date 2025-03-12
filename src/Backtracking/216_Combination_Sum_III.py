class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def getCombi(current,n,k,last,ans):
            print(current,n,k,last,ans)
            if k == 0 and n == 0:
                ans.append(current.copy())
                return
            else:
                for i in range(last+1,9):
                    if n - (i+1) < 0:
                        return
                    else:
                        current.append(i+1)
                        getCombi(current,n - (i+1),k-1,i,ans)
                        current.pop()
        
        getCombi([],n,k,-1,ans)

        return ans
            