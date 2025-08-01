class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        items.sort(key = lambda x: x[0])
        price_lower = items[0][0]

        price_lookup = [items[0]]

        # [a,b] up to point a, b is the best beauty
        for i in range(1,len(items)):
            if items[i][1] > price_lookup[-1][1] and items[i][0] == price_lookup[-1][0]:
                price_lookup[-1][1] = items[i][1]
            elif items[i][0] != price_lookup[-1][0]:
                price_lookup.append([items[i][0],max(items[i][1],price_lookup[-1][1])])

        res = []

        for query in queries:
            if query < price_lower:
                res.append(0)
            else:
                idx = bisect_right(price_lookup,query,key=lambda x: x[0])
                res.append(price_lookup[idx-1][1])
        

        return res

        # Memory Limit Exceeded solution

        # items.sort(key = lambda x: x[0])

        # price_range = (items[0][0],items[-1][0])

        # price_lookup = {}
        # idx = 0
        # last_max = 0
        # for i in range(price_range[0],price_range[1] + 1):
            
        #     if idx < len(items) and i < items[idx][0]:
        #         price_lookup[i] = last_max
        #     elif idx < len(items) and i == items[idx][0]:
        #         price_lookup[i] = last_max
        #         while idx < len(items) and items[idx][0] == i:
        #             price_lookup[i] = max(price_lookup[i],items[idx][1])
        #             idx += 1
        #         last_max = price_lookup[i]
        #     else:
        #         price_lookup[i] = last_max
        
        # res = []

        # for query in queries:
        #     if query < price_range[0]:
        #         res.append(0)
        #     else:
        #         res.append(price_lookup[query] if query < price_range[1] else price_lookup[price_range[1]])
        
        return res

                