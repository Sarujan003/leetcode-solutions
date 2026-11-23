def summaryRanges(nums):

    right, left = 0, 0
    output = []

    while right < len(nums):
        if right + 1 < len(nums) and nums[right] + 1 == nums[right + 1]:
            right += 1

        else:
            if left == right:
                output.append(f"{nums[left]}")
            else:
                output.append(f"{nums[left]}->{nums[right]}")
            right , left = right + 1, right + 1

    return output


nums = [0, 3, 4, 5, 7, 9]
print(summaryRanges(nums))