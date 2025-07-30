class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        #　find prime that is less than 1000

        smaller_prime = {0:0,1:0,2:0}
        last_prime = 2
        for i in range(3,1001):
            for j in range(2,isqrt(i)+1):
                if i%j == 0:
                    smaller_prime[i] = last_prime
                    break
            if i not in smaller_prime:
                smaller_prime[i] = last_prime
                last_prime = i
        

        nums[0] = (nums[0] - smaller_prime[nums[0]]) if nums[0] >= 1 else nums[0]
        for i in range(1,len(nums)):
            #print(nums)
            if nums[i] <= nums[i-1]:
                return False
            else:
                nums[i] = (nums[i] - smaller_prime[nums[i]-nums[i-1]]) if (nums[i] - nums[i-1]) >= 1 else nums[i]

        
        #print(nums)
        return True
                
            