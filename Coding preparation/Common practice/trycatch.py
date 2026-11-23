n = 10

try:
    n / 0

except ZeroDivisionError:
    print('Cant divide by zero')

finally:
    print('Execution completed!')