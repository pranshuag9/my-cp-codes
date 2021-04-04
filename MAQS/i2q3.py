"""
 @url: https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
 @problem: Given a string of lowercase alphabets, print the length of the longest palindromic subsequence that can be formed using the characters of the original string. Order of arrangement is not important. For example for string ‘bcbdcddcdac’, we can construct a palindromic string as ‘cdcbdadbcdc’.
 Algorithm:
 1. Initialize a dictionary
 2. for i:=0 to len(string), step by 1,
 3.     Add ith character of string to dictionary and set value to 1 if already present, else increment previous value corresponding to the key by 1
 4. Initialize result to empty string
 5. Sort the dictionary (key, value) pair by value in increasing order which returns a list in python.
 6. convert list to dictionary.
 7. for each key, value in items() of dictionary:
 8.     if result is empty string and value is 1, then concatenate key to result
 9.     while value is not 0 and 1, do
 10.        Concatenate key to starting and ending of result.
 11.        decrement value by 2
 12. return result
"""
def longest_palindromic_subsequence(string):
    dictionary = {}
    for i in range(len(string)): dictionary[string[i]] = dictionary.get(string[i], 0) + 1
    result = ""
    dictionary = sorted(dictionary.items(), key=lambda kv:(kv[1], kv[0]))
    dictionary = dict(dictionary)
    for key, value in dictionary.items():
        if result == "" and value == 1:
            result += key
            continue
        while value != 0 and value != 1:
            result = key + result + key
            value = value - 2
    return result

if __name__ == "__main__":
    string = input().strip()
    lps = longest_palindromic_subsequence(string)
    print(lps)