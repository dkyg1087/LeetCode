class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Have two pointers go from two ways from the string
        # Since the list is sorted, we just add the current two nubmers
        # If the number is too big we move the right one closer to the left and vice versa until we find the correct one
        
        left,right = 0,len(numbers)-1

        while True:
            temp = numbers[left]+ numbers[right]

            if temp > target:
                right -= 1
            elif temp < target:
                left += 1
            else:
                return [left+1,right+1]