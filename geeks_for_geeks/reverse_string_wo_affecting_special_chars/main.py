'''
 @url: https://www.geeksforgeeks.org/reverse-a-string-without-affecting-special-characters/

 Algorithm:
 1. take input string of size n
 2. l = 0, r = n - 1
 3. while(l < r) do
    1. if str[l] not alphabetic character then l++
    2. elseif str[r] not alphabetic character then r--
    3. else swap str[l++] and str[r--]
 4. print the string
'''
def reverse_string(string):
    l, r = 0, len(string) - 1
    while l < r:
        if not string[l].isalpha(): l += 1
        elif not string[r].isalpha(): r -= 1
        else:
            string[l], string[r] = string[r], string[l]
            l, r = l + 1, r - 1

def print_result(string):
    for char in string: print(char, end='')

if __name__ == "__main__":
    inp = "a!!!b.c.d,e'f,ghi" # input()
    string = [char for char in inp]
    reverse_string(string)
    print_result(string)