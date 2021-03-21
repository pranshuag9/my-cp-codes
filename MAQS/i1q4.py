"""
 @url: https://www.geeksforgeeks.org/maq-software-interview-experience-on-campus-placement-2021/
 @problem: Reverse the given string  and also reverse the every alternate word of string , for ex “i love to code” to “code ot love i” or “my name is xyz” to “xyz si name ym”.
 Algorithm(string):
 1. Reverse the string
 2. Create a wordlist by splitting the string by whitespace
 3. Initialize count = 0
 4. for i in 0 to len(wordlist) step by 2, reverse each string at i index
 5. return wordlist joined by " "
"""
def reverse_string(string):
    string = string[::-1]
    wordlist = string.split()
    for i in range(0, len(wordlist), 2):
        wordlist[i] = wordlist[i][::-1]
    return " ".join(wordlist)
if __name__ == "__main__":
    string = "i love to code" # input().strip()
    print(reverse_string(string))