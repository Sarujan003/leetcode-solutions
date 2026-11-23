class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        
        s = 0
        for i in nums:
            s += i

        actual = n*(n+1)/2

        return int(actual) - s