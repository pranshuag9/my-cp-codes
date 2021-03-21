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
        while(temp): count, temp = count + 1, temp.next
        return count

    def remove_at(self, index):
        if index < 0 or index > self.size():
            print("Index Out Of Bounds")
            return
        count, temp = 1, self.head
        while(count != index ): temp, count = temp.next, count + 1
        x = temp.next
        temp.next = temp.next.next
        del x

if __name__ == "__main__":
    ll = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
    print(ll)
    ll.remove_at(3)
    print(ll)