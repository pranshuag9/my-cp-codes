"""
 @url: https://www.geeksforgeeks.org/smallest-multiple-of-a-given-number-made-of-digits-0-and-9-only/
 Algorithm:
 1. Set MAX_COUNT to 10000 and create a empty vector_array
 2. Generate MAX_COUNT numbers using Queue and BFS
 3. Create a Queue and put "9" at rear end.
 4. Using for loop, start BFS traversal of tree with root node "9", left child "0" and right child "9" for MAX_COUNT to -1
    1. create s1 variable taking front element of queue
    2. empty first element from queue
    3. add s1 element to vector
    4. create s2 variable taking value of s1
    5. Append "0" to s1 and "9" to s2 as Left Child, Right Child
    6. Put s1 to queue, then put s2 to queue, because s1 < s2, i.e, 0 < 9
"""
from queue import Queue
MAX_COUNT, vector = 10000, []
def generateNumbersUtil():
    global vector
    q = Queue()
    q.put("9")
    for _ in range(0, MAX_COUNT + 1):
        s1 = q.queue[0]
        q.get()
        vector.append(s1)
        s2 = s1
        s1, s2 = s1 + "0", s2 + "9"
        q.put(s1)
        q.put(s2)
def findSmallestMultiple(n):
    global vector
    for i in range(len(vector)):
        if(int(vector[i]) % n == 0):
            return vector[i]
if __name__ == "__main__":
    generateNumbersUtil()
    n = 7 # int(input().strip())
    print(findSmallestMultiple(n))