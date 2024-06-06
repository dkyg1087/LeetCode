class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Every iteration count the alphabet appearence in each word
        # Use that as a key to categorize them into sets

        d = {}

        for s in strs:
            count = [0] * 26
            for c in s:

                # ord() returns the ASCII code of that char, we minus the ASCII code for 'a' so that it will fit into a list[26]

                count[ord(c)-ord('a')] += 1
                
            t = tuple(count)
            if t not in d:
                d[t] = [s]
            else:
                d[t].append(s)

        return d.values()