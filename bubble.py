a = [5,1,4,3,2]


for i in range(len(a) - 1):
    print("The array comes for processing :", a)
    for j in range(len(a) - i - 1):
        if a[j] > a[j+1]:
            temp = a[j + 1]
            a[j + 1] = a[j]
            a[j] = temp

    print("The array after processing :", a)


print(a)