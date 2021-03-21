class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def __str__(self):
        temp, result = self.head, ""
        while temp: result, temp = result + f"{temp.data}=>", temp.next
        return result + "null"

    def mid(self):
        if self.head is None: return "ll is empty!"
        slow, fast = self.head, self.head
        while fast and fast.next: slow, fast = slow.next, fast.next.next
        return slow

if __name__ == "__main__":
    ll = LinkedList()
    mid = ll.mid()
    if isinstance(mid, str): print(mid)
    else: print(mid.data)
    print("-----------------------")
    ll = LinkedList(Node(1))
    mid = ll.mid()
    print(ll)
    print(mid.data)
    print("-----------------------")
    ll = LinkedList(Node(1, Node(2)))
    mid = ll.mid()
    print(ll)
    print(mid.data)
    print("-----------------------")
    ll = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
    mid = ll.mid()
    print(ll)
    print(mid.data)
    print("-----------------------")