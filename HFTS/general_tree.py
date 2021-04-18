class Node:
    def __init__(self, data, childNodes=[]):
        self.childNodes = childNodes
        self.data = data
class Tree:
    def __init__(self, rootNode=None):
        self.rootNode = rootNode
    def get_node(self, node, data):
        if node.data == data: return node
        reqNode = None
        for cn in node.childNodes:
            if cn.data == data: return cn
            reqNode = self.get_node(cn, data)
            if reqNode != None: break
        return reqNode
    def display(self, data, rootNode=None):
        node = self.get_node(self.rootNode, data) if rootNode is None else rootNode
        if len(node.childNodes) == 0: return
        for cn in node.childNodes:
            print(cn.data, end=' ')
            self.display(data, rootNode=cn)
    def add(self, data, newData):
        if self.rootNode is None:
            self.rootNode = Node(newData, [])
            return self.rootNode
        parentNode = self.get_node(self.rootNode, data)
        newNode = Node(newData, [])
        parentNode.childNodes.append(newNode)
        return newNode
if __name__ == "__main__":
    tree = Tree()
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        root, data = input().split(" ")
        tree.add(root, data)
    dispNode = input("Enter node to display: ")
    tree.display(dispNode)

"""
8
 A
A B
A C
A D
B E
B F
F G
F H
F
"""