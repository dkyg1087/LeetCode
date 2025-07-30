class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        
        def add_to_dict(dic,number):
            if number not in dic:
                dic[number] = 1
            else:
                dic[number] += 1
        
        def remove_from_dict(dic,number):
            if dic[number] == 1:
                del dic[number]
            else:
                dic[number] -= 1

        
        c = Counter(candies)
        window = {}
        for i in range(k):
            add_to_dict(window,candies[i])
            remove_from_dict(c,candies[i])

        res = len(c) 
        left,right = 0,k-1
        for _ in range(k,len(candies)):
            right += 1
            add_to_dict(window,candies[right])
            remove_from_dict(c,candies[right])
            add_to_dict(c,candies[left])
            remove_from_dict(window,candies[left])
            left += 1
            res = max(res,len(c))
        
        return res
            

            
        
        
        
            

        