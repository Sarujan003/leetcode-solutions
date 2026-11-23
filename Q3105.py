# class Solution:
#     def longestMonotonicSubarray(self, nums: List[int]) -> int:
#         j = 0

#         count = 1

#         if len(nums) == 1:
#             return count

#         for i in range(1,len(nums)):
#             if nums[j] + (i-j) != nums[i]:
#                 j = i

#             count = max(count, i+1-j)

#         j = 0

#         for i in range(1,len(nums)):
#             if nums[j] - (i-j) != nums[i]:
#                 j = i

#             count = max(count, i+1-j)

#         return count



def longestMonotonicSubarray(nums):
    j = -1

    c = 0
    count = 1

    if len(nums) == 1:
        return count

    for i in range(1,len(nums)):
        if nums[i] - nums[i-1] > 0:
            if c!= nums[i] - nums[i-1]:
                c = nums[i] - nums[i-1]
                count = max(count, i-j)
                j = i - 1

        else:
            c = 0
            count = max(count, i-j)
            j = i - 1

    return count



nums = [1,4,7,8,9]

print(longestMonotonicSubarray(nums))
