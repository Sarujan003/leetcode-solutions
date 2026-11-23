x = 1001

y = list(str(x))
mid = int(len(y) / 2) - 1

print(y)
print(mid)
print(y[:mid+1], y[len(y)-mid -1:][::-1])
if (y[:mid+1] == y[len(y)-mid -1:][::-1]):
    print(True)

else:
    print(False)