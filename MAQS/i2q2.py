"""
 @url: https://www.geeksforgeeks.org/number-of-pairs-in-an-array-with-the-sum-greater-than-0/
 @problem: Given an array arr[] of size N, the task is to find the number of distinct pairs in the array whose sum is > 0.
 Algorithm for lower_bound(arr, value):
 1. for i:=0 to len(arr):
 2.     if arr[i] >= value:
 3.         return i

 Algorithm for findNumOfPair(arr, n):
 1. Convert the array to set
 2. Sort the set arr and initialize count = 0
 3. for i:=0 to len(arr), step by 1,
 4.     if arr[i] is negative, then continue
 5.     otherwise, Increment count by difference between (current element index i) and lower_bound element of (negative of current element + 1)
 6. return count
"""
def lower_bound(arr, value):
    for i in range(len(arr)):
        if arr[i] >= value: return i
def findNumOfPair(a, n):
    a, cnt = sorted(set(a)), 0
    for i in range(n): cnt = cnt if(a[i] <= 0) else cnt  + (i - lower_bound(a, -a[i] + 1))
    return cnt
if __name__ == '__main__':
    a = [3, -2, 1]
    n = len(a)
    count = findNumOfPair(a, n)
    print(count)