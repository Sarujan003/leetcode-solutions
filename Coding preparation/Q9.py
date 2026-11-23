def find_first_non_repeat_char(string):
    counter = {}

    for s in string:
        counter[s] = counter.get(s,0) + 1

    for c in counter:
        if counter[c] == 1:
            return c

    return None

print(find_first_non_repeat_char('akacblbc'))