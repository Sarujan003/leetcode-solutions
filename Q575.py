class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        unique = set()

        for i in candyType:
            if i not in unique:
                unique.add(i)

        return min(len(unique), len(candyType)//2)