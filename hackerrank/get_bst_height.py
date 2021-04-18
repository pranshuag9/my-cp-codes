class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None
class Solution:
    def insert(self, root, data):
        if root == None: return Node(data)
        if data <= root.data: root.left = self.insert(root.left, data)
        else: root.right = self.insert(root.right, data)
        return root
    def getHeight(self, root):
        if root is None: return -1
        leftDepth = self.getHeight(root.left)
        rightDepth = self.getHeight(root.right)
        return leftDepth + 1 if leftDepth > rightDepth else rightDepth + 1

if __name__ == "__main__":
    T = int(input())
    myTree = Solution()
    root = None
    for i in range(T):
        data = int(input())
        root = myTree.insert(root, data)
    height = myTree.getHeight(root)
    print(height)

"""
7
3
5
2
1
4
6
7
"""