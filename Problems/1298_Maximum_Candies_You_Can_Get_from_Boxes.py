class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        candy_count = 0
        opened = [False] * len(status)
        seen = [False] * len(status)
        have_keys = {}
        que = deque(initialBoxes[:])

        while que:
            
            box = que.popleft()
            if opened[box]:
                continue
            
            if (status[box] == 1) or (box in have_keys):
                opened[box] = True
                candy_count += candies[box]
                que.extend(containedBoxes[box])
                for key in keys[box]:
                    have_keys[key] = True
            else:
                if not seen[box]:
                    seen[box] = True
                    que.append(box)
        
        return candy_count