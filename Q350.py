from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # output = []

        # j = 0
        # i = 0

        # nums1.sort()
        # nums2.sort()

        # while j<len(nums1) and i<len(nums2):
        #     if nums1[j] == nums2[i]:
        #         output.append(nums1[j])
        #         j += 1
        #         i += 1
                

        #     elif nums1[j] < nums2[i]:
        #         j += 1

        #     else:
        #         i += 1

        # return output

        output = []

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        count = Counter(nums1)

        for num in nums2:
            if count[num] > 0:
                output.append(num)
                count[num] -= 1

        return output

        