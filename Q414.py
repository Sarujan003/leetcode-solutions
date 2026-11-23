class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first, second, third = None, None, None

        for n in nums:
            if (first is None) or (n > first):
                first, second, third = n, first, second

            elif (n!=first) and (second is None or n>second):
                second, third = n, second

            elif (n!=first) and (n!=second) and (third is None or n>third):
                third = n

        if third is not None:
            return third

        elif first is not None:
            return first

        else:
            return None