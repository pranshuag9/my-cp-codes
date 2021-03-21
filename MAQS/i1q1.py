"""
 @url: https://www.geeksforgeeks.org/maq-software-assessment-interview-experience-on-campus-2021/
 @problem: given a string at the end of which the length of string was given(there can be blank spaces also at the end), find the length of the actual string(excluding the last part, which is the actual string length eg “abcd 36”, o/p -> 6)
 Algorithm(string, str_len(type=string)):
 1. Create a new_string from 0 to n - 1 by slicing string
 2. get last digit from string using slicing
 3. concatenate last digit at start of str_len
 4. If Integer value of str_len equals new_string_length, then return str_len and new_string(for printing purpose)
 5. Recursively return the function get_str_len passing (new_string and str_len)
"""
def get_str_len(string, str_len=""):
    new_string = string[:-1]
    str_len, new_string_len = string[-1] + str_len, len(new_string)

    if int(str_len) == new_string_len: return int(str_len), new_string
    return get_str_len(new_string, str_len)

if __name__ == "__main__":
    string = "abcd 36   ".rstrip() # input().rstrip()
    result = get_str_len(string)
    print(f"{result[1]}\nActual String Length is:", result[0])
    print("----------------------")

    string = "0   ".rstrip()  # input().rstrip()
    result = get_str_len(string)
    print(f"{result[1]}\nActual String Length is:", result[0])
    print("----------------------")

    string = "abcdefghi 10   ".rstrip()  # input().rstrip()
    result = get_str_len(string)
    print(f"{result[1]}\nActual String Length is:", result[0])
    print("----------------------")

    string = "abcdefghijkl 114   ".rstrip()  # input().rstrip()
    result = get_str_len(string)
    print(f"{result[1]}\nActual String Length is:", result[0])
    print("----------------------")