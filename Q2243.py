def digitSum(s, k):
        while (len(s)>k):
            summation = 0
            modify = ""
            j = 0
            for i in range(len(s)):
                summation = summation + int(s[i])
                j = j + 1

                if j == k:
                    j = 0
                    modify = modify + str(summation)
                    summation = 0

            if j != 0:
                modify = modify + str(summation)
            s = modify

        return s

s = "1234"
k = 2
print(digitSum(s, k))