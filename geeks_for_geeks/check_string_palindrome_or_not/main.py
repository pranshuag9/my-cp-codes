"""
 @url:https://www.geeksforgeeks.org/python-program-to-check-if-number-is-palindrome-one-liner/
"""
if __name__ == "__main__":
    string = "rotator" # input()
    print("PALINDROME") if (lambda x: True if x == x[::-1] else False) else print("NOT A PALINDROME")