"""
 @url: https://www.geeksforgeeks.org/write-a-program-to-reverse-digits-of-a-number/
 @problem: Given a number, reverse its digits
 Algorithm:
 1. Take number n as input
 2. Set result = 0
 3. while n not equals 0, loop over
        remainder = n % 10
        result = 10*result + remainder
        n = floor(n/10)
 4. return result
"""
# Reversing digits using string slicing
def reverse_digits(n):
    return int(str(n)[::-1])
# Reversing digits using given algorithm
def reverse_digitsI(n):
    result = 0
    while n is not 0:
        result = 10 * result + (n % 10)
        n = n // 10
    return result
if __name__ == "__main__":
    n = int(input().strip())
    print(reverse_digitsI(n))