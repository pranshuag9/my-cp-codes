"""
 @url: https://www.geeksforgeeks.org/java-program-for-program-for-fibonacci-numbers/
 @problem: n-th Fibonacci numbers
"""
# Using Recursion
def fibr(n):
    if n<=1: return n
    return fibr(n - 1) + fibr(n - 2)
# Using DP
def fibdp(n):
    f = [0,1]
    for i in range(2, n + 1): f.append(f[i - 1] + f[i - 2])
    return f[n]
# Using DP with Space optimization
def fib(n):
    b, a, c = 0, 1, None
    for _ in range(2, n + 1):
        c = a + b
        b, a = a, c
    return c
if __name__ == "__main__":
    n = 9 # int(input())
    nth_fib = fib(n)
    print(nth_fib)