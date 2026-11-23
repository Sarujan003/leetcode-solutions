data = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

x = list(input())

num = 0

value_array = []

print(x)

if len(x) == 1:
    num = data[x[0]]
    print(num)
else:
    for i in x:
        value_array.append(data[i])


    print(value_array)

    for n in range(len(value_array)-1):
        print(n)
        if n >= 0:
            if value_array[n] < value_array[n+1]:
                value_array[n] = -1 * value_array[n]

    print(sum(value_array))





