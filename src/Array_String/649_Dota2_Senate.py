class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_count = senate.count("R")
        d_count = len(senate) - r_count
        score = 0

        queue = deque(senate)
        
        while r_count and d_count:
            sen = queue.popleft()

            if sen == "R":
                if score >= 0:
                    score += 1
                    queue.append("R")
                else:
                    score += 1
                    r_count -= 1
            else:
                if score <= 0:
                    score -= 1
                    queue.append("D")
                else:
                    score -= 1 
                    d_count -= 1
        
        if r_count == 0:
            return "Dire"
        else:
            return "Radiant"
        


        
        


        