def findDisappearedNumbers(nums):
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -1 * nums[abs(nums[i]) - 1]

        output = []

        for i in range(len(nums)):
            if nums[i] > 0:
                output.append(i+1)

        return output

nums = [4, 3, 2, 7, 8, 2, 3, 1]

print(findDisappearedNumbers(nums))