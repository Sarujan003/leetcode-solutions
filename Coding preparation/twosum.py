# let me define a function named as TwoSum, and it has to get the 2 variable as input based on the problem scenario
def TwoSum(lst, target):
    #  then i am going to initialize a dictionary named seen to keep track the array element
    seen = dict()
    #  the key of this dictionary will be the value of the array elements and value will be the index of the element

    for i in range(len(lst)):
        complement = target - lst[i]

        if complement in seen:
            return seen[complement], i

        else:
            seen[lst[i]] = i

    return -1, -1


lst = [1,2,3,4,5]
target = 8
ind1, ind2 = TwoSum(lst, target)

print(f'{lst[ind1]} + {lst[ind2]} = {target}')
