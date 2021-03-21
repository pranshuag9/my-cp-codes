class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def __str__(self):
        result, temp = "", self.head
        while temp: result, temp = result + f"{temp.data}=>", temp.next
        return result + "null"

    def delete_node(self, node):
        if node.next is None:
            del node
            return
        x = node.next
        node.data = node.next.data
        node.next = node.next.next
        del x
if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    ll = LinkedList(node1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    print(ll)
    print("-----------")
    ll.delete_node(node4)
    print(ll)
    # Unfortunately, it is not working when the last node is given as input for deletion because its reference is stored in previous node which we can't access without head reference
    print("-----------")
