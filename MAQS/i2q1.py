"""
 @url: https://www.geeksforgeeks.org/maq-software-assessment-interview-experience-on-campus-2021/
 @problem: given a paragraph in the form of a string, print the words in the paragraph in decreasing order of their frequency
 Algorithm(string):
 1. Create a wordlist by removing whitespaces from start and end of string and splitting it by whitespaces
 2. Initialize dictionary and result variables
 3. for each word in wordlist, add word to dictionary and increment value by 1 or get previous value and increment by 1
 4. sort each (key, value) pair in dictionary by value's in dictionary in decreasing order
 5. concatenate each key of dictionary to result separated by blank space
 6. return result
"""
def frequency_paragraph(string):
    wordlist = string.strip().split()
    dictionary, result = {}, ""
    for word in wordlist: dictionary[word] = dictionary.get(word, 0) + 1
    dictionary = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
    for item in dictionary.keys(): result += item + " "
    return result

if __name__ == "__main__":
    string = "given a paragraph in the form of a string, print the words in the paragraph in decreasing order of their frequency".lower()
    result = frequency_paragraph(string)
    print(result)