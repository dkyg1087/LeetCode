class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        c = list(c.values())
        if len(c) == len(set(c)):
            return True
        else:
            return False