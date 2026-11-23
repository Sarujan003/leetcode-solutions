from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = dict(Counter(nums))

        for d in count:
            if count[d] > len(nums) / 2:
                return d


