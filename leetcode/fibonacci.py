def fib(self, N: int) -> int:
    n, m = 0, 1
    for i in range(1, N):
        n, m = m, n + m
    return 0 if N == 0 else m
