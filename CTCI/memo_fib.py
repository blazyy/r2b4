def memo_fib(n):
    memo = [0] * n
    for i in range(n):
        print(i, ': ', fib(i, memo))

def fib(n, memo):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif memo[n] > 0:
        return memo[n]

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


memo_fib(20)
