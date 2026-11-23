def Binary_Search(lst, target):

    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = (first + last) // 2

        if lst[mid] == target:
            return mid

        if target < lst[mid]:
            last = mid - 1

        elif target > lst[mid]:
            first = mid + 1

    return -1

print(Binary_Search([1,5,8,11,16], 8))