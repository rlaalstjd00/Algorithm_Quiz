import sys
input = sys.stdin.readline

n = int(input())
memo = [0 for i in range(100)]

def f(n):
    if n<= 1:
        return n
    else:
        if memo[n] > 0:
            return memo[n]
        memo[n] = f(n-1) + f(n-2)
        return memo[n]

print(f(n))

