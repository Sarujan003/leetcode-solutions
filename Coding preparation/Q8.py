def remove_duplicate(lst):
    output = []

    for n in lst:

        if n not in output:
            output.append(n)


    return output

print(remove_duplicate([3,1,3,2,1,5]))