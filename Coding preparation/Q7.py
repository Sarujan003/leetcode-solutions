def second_largest(lst):
    first, second = None, None

    for n in lst:

        if first is None or n > first:
            first, second = n, first

        elif n != first and (second is None or n > second):
            second = n

    return second

print(second_largest([3,3]))