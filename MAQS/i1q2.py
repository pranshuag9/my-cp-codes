"""
 @url: https://www.geeksforgeeks.org/maq-software-assessment-interview-experience-on-campus-2021/
 @problem: check the given string is palindrome or not using RECURSION ONLY
 Algorithm(string, start, end):
 1. if length of string is 0 or 1 then return True
 2. store starting and ending character of string in char1 and char2
 3. if char1 == char2, then return check_palindrome(string excluding starting and ending character, start + 1, end - 1)
 4. else return False
"""
def check_palindrome(string, start, end):
    if len(string) in (0, 1): return True
    char1, char2 = string[start], string[end]
    return check_palindrome(string[start + 1 : end], start + 1, end - 1) if char1 == char2 else False

if __name__ == "__main__":
    string = "rotator" # input().strip()
    print(f"{string} is PALINDROME") if check_palindrome(string, 0, -1) else print(f"{string} is NOT A PALINDROME")