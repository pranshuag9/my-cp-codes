"""
 @url: https://www.geeksforgeeks.org/count-permutations-possible-by-replacing-characters-in-a-binary-string/
 @problem: Given a string S consisting of characters 0, 1, and ‘?’, the task is to count all possible combinations of the binary string formed by replacing ‘?’ by 0 or 1.
 Algorithm:
 Count the number of ? characters in string. Since ? can be replaced only by 0 or 1, so total permutations possbile are 2^count
 1. Create count = 0
 2. for every character in string:
 3. if character equals "?", then, increment count
 4. return 2^count
"""
def count_permutations(string):
    count = 0
    for i in string:
        if i == "?": count += 1
    return (2**count)
if __name__ == "__main__":
    string = input()
    print(count_permutations(string))