"""
 @url: https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
 Algorithm(index, data):
 1. if index < 0 or index > size_of_linkedlist then return "Index out of bound"
 2. count, temp = 0, head
 3. while count!=index and temp.next is not None: then, temp, count = temp.next, count + 1
 4. temp.next = Node(data, temp.next)
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def __str__(self):
        result, temp = "", self.head
        while(temp): result, temp = result + f"{temp.data}=>", temp.next
        return result + "null"

    def size(self):
        count, temp = 0, self.head
        while(temp): temp, count = temp.next, count + 1
        return count

    def insert_after_index(self, index, data):
        if index < 0 or index > self.size():
            print("Index Out of Bound")
            return
        count, temp = 0, self.head
        while(count != index and temp.next is not None): temp, count = temp.next, count + 1
        temp.next = Node(data, temp.next)

if __name__ == "__main__":
    ll = LinkedList(Node(1,Node(2, Node(3, Node(4)))))
    print(ll)
    ll.insert_after_index(2, data=10)
    print(ll)
    ll.insert_after_index(2, data=5)
    print(ll)