"""
 @url: https://www.geeksforgeeks.org/program-decimal-binary-conversion/
 @problem: Given a decimal number as input, we need to write a program to convert the given decimal number into equivalent binary number.
 Algorithm(decimal):
 1. Store the remainder when the number is divided by 2 in an array.
 2. Divide the number by 2
 3. Repeat the above 2 steps until the number is greater than zero.
 4. Print the array in reverse order now.
"""
def dec_2_bin(decimal):
    binary = []
    while decimal>0:
        rem = str(decimal % 2)
        binary = [rem]+binary if binary else [rem]
        decimal = decimal // 2
    return "".join(binary)
if __name__ == "__main__":
    decimal = int(input().strip())
    binary = dec_2_bin(decimal)
    print(binary)