def Factorial(N):
    if (N <= 1):
        return 1
    else:
        return N * Factorial(N-1)

print(Factorial(int(input())))
