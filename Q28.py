haystack = "hello"
needle = "ll"


for i in range(len(haystack) - len(needle) + 1):
    bool = True

    for j in range(len(needle)):

        if haystack[i+j] != needle[j]:
            bool = False
            break

    if bool:
        print(i)
        break


