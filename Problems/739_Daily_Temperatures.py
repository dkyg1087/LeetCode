class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStk = []
        ans = deque()
        for i in range(len(temperatures)-1,-1,-1):
            while len(monoStk) > 0  and temperatures[monoStk[-1]] <= temperatures[i]:
                monoStk.pop()
            if len(monoStk) == 0:
                ans.appendleft(0)
            else:
                ans.appendleft(monoStk[-1] - i)
            
            monoStk.append(i)
        
        return list(ans)
            