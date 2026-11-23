s = "abbaccd"

# find the unique characters
unique_c = set(s)

output = []

for c in unique_c:
    s_index = s.index(c)
    e_index = len(s) - s[::-1].index(c) - 1

    print(c, s_index, e_index, s.count(c))

    if (e_index - s_index + 1 == s.count(c)):
        output.append(s[s_index:e_index+1])

print(output)


