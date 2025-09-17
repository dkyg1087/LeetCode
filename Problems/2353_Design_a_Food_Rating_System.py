import heapq

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.type_dict = defaultdict(list)
        self.food_score = {}

        for i in range(len(foods)):
            self.food_score[foods[i]] = [-ratings[i],cuisines[i]]
            heapq.heappush(self.type_dict[cuisines[i]],(-ratings[i],foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_score[food][0] = -newRating
        food_type = self.food_score[food][1]
        heapq.heappush(self.type_dict[food_type],(-newRating,food))
        

    def highestRated(self, cuisine: str) -> str:
        while True:
            targ = self.type_dict[cuisine]
            
            if targ[0][0] != self.food_score[targ[0][1]][0]:
                heapq.heappop(self.type_dict[cuisine])
            else:
                break
        
        return self.type_dict[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)