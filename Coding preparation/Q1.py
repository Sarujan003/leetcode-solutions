string = input()

# def reverse_string(string):
#     return string[::-1]

# def reverse_string(string):

#     output = []

#     for i in range(len(string)):

#         output.append(string[len(string)- i - 1])

#     return "".join(output)


# print(reverse_string(string))


def is_palindrome(string):

    return string == string[::-1]


print(is_palindrome(string))
