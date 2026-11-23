class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        j = 0

        for i in range(len(flowerbed)):
            if n == 0:
                break
            if flowerbed[i] == 1:
                if i+1 < len(flowerbed):
                    j = i + 1

            else:
                if len(flowerbed) == 1:
                    n = n - 1
                elif i-j == 2:
                    j = i
                    n = n - 1

                elif i == 1 and j == 0:
                    j = i
                    n = n - 1

                elif i == len(flowerbed) - 1 and j == len(flowerbed) - 2:
                    n = n - 1

        return n == 0

            
            

