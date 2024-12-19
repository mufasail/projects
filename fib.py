fib1 = 1
fib2 = 1
fib_sum = 0
max = int(input("max:"))
while fib2 < max:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    print(fib2)
