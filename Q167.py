class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        # Key point is, the array is already sorted
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1

            elif numbers[left] + numbers[right] < target:
                left += 1

            else:
                return [left+1, right+1]