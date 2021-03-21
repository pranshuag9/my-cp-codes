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
    def pop(self):
        self.head = self.head.next
if __name__ == "__main__":
    ll = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
    print(ll)
    ll.pop()
    print(ll)