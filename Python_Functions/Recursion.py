def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


factorial = fact(5)
print('Factorial of 5 is', factorial)
