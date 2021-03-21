def get_union(arr1, arr2):
    return [item for item in arr1 if(item in arr2) or (item not in arr2)]+[item for item in arr2 if(item not in arr1)] # list(set().union(arr1, arr2))

def get_intersection(arr1, arr2):
    return [item for item in arr1 if item in arr2]

if __name__ == "__main__":
    arr1 = [7, 1, 5, 2, 3, 6] # input().strip().split()
    arr2 = [6, 8, 3, 20, 7] # input().strip().split()
    union = get_union(arr1, arr2)
    intersection = get_intersection(arr1, arr2)

    print("Array 1:", arr1)
    print("Array 2:", arr2)
    print("Union:", union)
    print("Intersection:", intersection)