class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = [False] * len(bank)

        queue = deque([startGene])

        if endGene not in bank:
            return -1
        
        step = 1

        while queue:
            length = len(queue)
            for _ in range(length):
                targ = queue.popleft()
                for i in range(len(bank)):
                    if visited[i] or sum([targ[j] != bank[i][j] for j in range(8)]) != 1:
                        continue
                    
                    if bank[i] == endGene:
                        return step
                    else:
                        visited[i] = True
                        queue.append(bank[i])
            
            step += 1
                    
                    

                        
        return -1
            

        