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

    def remove(self):
        if not self.head: return
        elif not self.head.next:
            self.head = None
            return
        temp = self.head
        while(temp.next.next): temp = temp.next
        temp.next = None

if __name__ == "__main__":
    ll = LinkedList()
    ll.remove()
    print(ll)
    print("-------------------------")
    ll.head = Node(1)
    print(ll)
    ll.remove()
    print(ll)
    print("-------------------------")
    ll.head = Node(1, Node(2))
    print(ll)
    ll.remove()
    print(ll)
    print("-------------------------")