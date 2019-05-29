def fib(a):
    n, m = 1, 0
    for i in range(a):
        n, m = n + m, n
    return n

nmb = int(input())

print(nmb, ". elementem ciągu Fibbonaciego jest:", fib(nmb))