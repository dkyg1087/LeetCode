class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # We go from either side with two pointers
        # Save a max_size to store the max size seen
        # Every iteration we find the min of two and go in by one to find potential larger container
        
        i, j = 0, len(height)-1
        max_size = 0
        while i != j:
            max_size = max(max_size,(j-i)*min(height[i],height[j]))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        
        return max_size