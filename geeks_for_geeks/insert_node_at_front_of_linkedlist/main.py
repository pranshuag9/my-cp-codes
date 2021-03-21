'''
 @url: https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def __str__(self):
        result = ""
        temp = self.head
        while(temp):
            result = result + f"{temp.data}=>"
            temp = temp.next
        return result + "null"

    def push(self, data):
        self.head = Node(data, self.head)

if __name__ == "__main__":
    ll = LinkedList()
    ll.push(10)
    ll.push(20)
    print(ll)