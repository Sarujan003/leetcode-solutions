def two_sum(lst, num):
    seen = {}

    for i in range(len(lst) -1):

        left = num - lst[i]

        if left in lst[i+1:len(lst)]:

            return lst[i], left

    return None

print(
    two_sum(
        [1,2],
        1
    )
)