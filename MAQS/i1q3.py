"""
 @url: https://www.geeksforgeeks.org/count-pairs-with-given-sum/
 @problem: Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’.
 Algorithm(arr, sum):
 1. Initialize dictionary and result variables
 2. for each item in arr, add it to dictionary and increment by 1 or increment by previous_count + 1
 3. for each (key, value) pair in dictionary, do
    1. if key not equal to (sum-key) and (sum-key) present in dictionary
        1. Increment result by dictionary[key]*dictionary[sum-key]
        2. Reset dictionary[key] to 0
        3. Reset dictionary[sum-key] to 0
    2. else if key equals to (sum-key) and (sum-key) present in dictionary
        1. Increment result by dictionary[key]*(dictionary[key]-1)/2
        2. Set dictionary[key] = 0
 4. return result
"""
def get_pairs_count(arr, sum):
    dictionary, result = {}, 0
    for item in arr: dictionary[item] = dictionary.get(item, 0) + 1
    for key, value in dictionary.items():
        if (key != sum - key) and ((sum - key) in dictionary): result, dictionary[key], dictionary[sum - key] = result + (dictionary[key] * dictionary[sum - key]), 0, 0
        elif (key == sum - key) and ((sum - key) in dictionary): result, dictionary[key] = result + int((dictionary[key] * (dictionary[key] - 1)) / 2), 0
    return result

if __name__ == "__main__":
    arr = [1, 5, 7, -1, 5] # input().strip().split()
    sum = 6 # int(input().strip())
    print(arr, sum)
    print(get_pairs_count(arr, sum))
    print("--------------------------")
    arr = [1, 1, 1, 1]  # input().strip().split()
    sum = 2  # int(input().strip())
    print(arr, sum)
    print(get_pairs_count(arr, sum))
    print("--------------------------")