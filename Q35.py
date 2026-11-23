nums = [1,3,5,6]
target = 7

first = 0
last = len(nums) - 1

while True:
    mid = (first + last) // 2

    if nums[mid] > target:
        last = mid - 1

    elif nums[mid] < target:
        first = mid + 1

    if nums[mid] == target:
        print(mid)
        break

    if first > last:
        print(first)
        break

