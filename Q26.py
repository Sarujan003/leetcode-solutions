class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 0

        if len(nums) == 0:
            return 0

        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                nums[j+1] = nums[i]
                j += 1


        return j+1

