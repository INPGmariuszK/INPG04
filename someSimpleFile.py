def fib(a):
    n, m = 1, 0
    for i in range(a):
        n, m = n + m, n
    print( n )

fib(int(input())