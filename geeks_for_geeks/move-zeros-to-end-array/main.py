'''
 @url: https://www.geeksforgeeks.org/move-zeroes-end-array/
 Algorithm:
 1. count = 0
 2. for i:=0 to arr.length - 1 do
 3. if arr[i] != 0 then arr[count++] = arr[i]
 4. while count < arr.length do arr[count++] = 0
'''
def move_zeros_to_end(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < len(arr):
        arr[count] = 0
        count += 1
if __name__ == "__main__":
    arr = [3,23,5,0,2,4,0,1,0,30,6,74,0,8,0,9,0] # input().split(
    move_zeros_to_end(arr)
    print(arr)