"""
 @url: https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
 Algorithm(data):
 1. If head is null then head=node(data) and return
 2. temp = self.head
 3. while temp.next is not null do temp=temp.next
 4. temp.next = node(data)
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

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        temp = self.head
        while(temp.next): temp = temp.next
        temp.next = Node(data)

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    print(ll)