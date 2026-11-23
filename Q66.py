digits = [9,8,9]

# digit_placement = 1
# n = len(digits)

# num = 0

# for i in range(n):
#     digit_placement = 10 ** (i)
#     num = num + digit_placement * digits[n - i -1]


# num = num + 1

# output = []

# if sum(digits) == n * 9:
#     n += 1


# for i in range(n):
#     digit_placement = 10 ** (n-i-1)
#     number = num // digit_placement
#     output.append(number)

#     num = num % digit_placement

# print(output)

num_digit = len(digits)
curry = 0

if digits[-1] < 9:
    digits[-1] = digits[-1] + 1

else:
    for i in range(num_digit):
        if digits[num_digit - i - 1] == 9:
            digits[num_digit - i - 1] = 0
            curry = 1
        else:
            if curry == 1:
                digits[num_digit - i - 1] += 1
                curry = 0

        if curry == 0:
            break

    if curry == 1:
        print( [1] + [0] * num_digit)
        
print(digits)
