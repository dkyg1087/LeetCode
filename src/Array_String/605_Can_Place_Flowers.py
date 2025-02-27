class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        max_flower = 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                max_flower = 1
            return n <= max_flower

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    max_flower += 1
                elif i == len(flowerbed)-1 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    max_flower += 1
                elif i != 0 and i != len(flowerbed)-1 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    max_flower += 1

        return n <= max_flower