class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        start = 0

        if len(s) != len(goal):
            return False

        while start != len(s):
            for i in range(len(goal)):
                if s[(start + i) % len(s)] != goal[i]:
                    break
                
                if i == len(goal) - 1:
                    return True
            
            start += 1
        
        return False