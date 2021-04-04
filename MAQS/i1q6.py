"""
 @url: https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
 @problem: Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.
 Algorithm(arr):
 1. Initialize 3 counter for 0s, 1s, 2s in the array
 2. for i in arr:
 3.     if i==0: Increment c0 by 1
 4.     if i==1: Increment c1 by 1
 5.     if i==2: Increment c2 by 1
 6. c1 = c0+c1, c2 = c1+c2
 7. for i:=0 to len(arr):
 8.     arr[i] = 0 for i less than c0, 1 for i less than c1, 2 for i less than c2
 9. return arr
"""
def sortArray(arr):
    c0, c1, c2 = 0, 0, 0
    for i in arr:
        if i is 0: c0 += 1
        elif i is 1: c1 += 1
        else: c2 += 1
    c1, c2 = c0 + c1, c1 + c2
    for i in range(len(arr)):
        arr[i] = 0 if i < c0 else 1 if i < c1 else 2
    return arr
if __name__ == "__main__":
    arr = [int(i) for i in input().strip().split()]
    print(sortArray(arr))