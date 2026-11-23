a = "11"
b = "1"

data1 = {'1': 1, '0': 0}
data2 = {1: '1', 0: '0'}

carry = 0
output = []

i = len(a)
j = len(b)

while True:
        s = data1[a[i-1]] + data1[b[j-1]] + carry

        i -= 1
        j -= 1

        digit = s % 2

        output.append(data2[digit])

        carry = s // 2

        if i==0 or j==0:
            break

if i == 0:
    while j != 0:
        s = data1[b[j-1]] + carry
        j -= 1

        digit = s % 2

        output.append(data2[digit])

        carry = s // 2

if j == 0:
    while i != 0:
        s = data1[a[i-1]] + carry

        i -= 1

        digit = s % 2

        output.append(data2[digit])

        carry = s // 2

if carry == 1:

    output.append(data2[carry])


print(''.join(reversed(output)))