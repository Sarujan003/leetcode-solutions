def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


print(check_anagram('c*at', 'act'))