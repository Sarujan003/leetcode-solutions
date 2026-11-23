def generate_fib(num):
    f1 = 0
    f2 = 1

    if num == 0:
        return f1

    if num == 1:
        return f2

    for n in range(2,num+1):
        f1, f2 = f2, f1 + f2

    return f2

print(generate_fib(8))

