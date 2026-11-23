n = 19

seen = set()

while True:
    sq = 0

    while n != 0:
        sq = sq + (n%10) **2
        n = n // 10

    n = sq

    if sq == 1:
        print(True)
        break

    if sq not in seen:
        seen.add(sq)

    else:
        print(False)
        break