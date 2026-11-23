def checkString(s: str) -> bool:
    j = 0

    for i in range(1,len(s)):
        if s[j:i+1] == 'ba':
            return False

        j += 1

    return True

s = "aaba"

checkString(s)