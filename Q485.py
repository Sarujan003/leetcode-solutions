class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        m = 0
        for i in nums:
            if i == 1:
                count += 1
                if count > m:
                    m = count

            else:
                count = 0

        return m