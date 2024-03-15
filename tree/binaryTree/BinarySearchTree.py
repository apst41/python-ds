import queue
from collections import deque, OrderedDict


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Pair:
    def __init__(self, node, level):
        self.node = node
        self.level = level


class BinarySearchTree:
    def __init__(self):
        self.count = None
        self.ans = None
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        
        self.helper(self.root, data)
        return self.root
    
    def helper(self, root, data):
        if root is None: return Node(data)
        
        if data < root.data:
            root.left = self.helper(root.left, data)
        if data > root.data:
            root.right = self.helper(root.right, data)
        return root
    
    def insertIteration(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        root = self.root
        while root is not None:
            if data < root.data:
                if root.left is None:
                    root.left = Node(data)
                    return self.root
                else:
                    root = root.left
            else:
                if root.right is None:
                    root.right = Node(data)
                    return self.root
                else:
                    root = root.right
        return self.root
    
    def print_inorder(self, root):
        if root is None:
            return root
        self.print_inorder(root.left)
        print(root.data)
        self.print_inorder(root.right)
    
    def nth_largest_element(self, root, element):
        self.count = 0
        self.customDfs(root, element)
        return self.ans
    
    def customDfs(self, root, element):
        if root is None:
            return -1
        
        self.customDfs(root.left, element)
        self.count += 1
        if element == self.count:
            self.ans = root.data
            return
        self.customDfs(root.right, element)
    
    def topView(self, root):
        if root is None:
            return
        tree_map = OrderedDict()
        myqueue = deque()
        myqueue.append(Pair(root, 0))
        
        while myqueue:
            mypair = myqueue.popleft()
            if mypair.level not in tree_map:
                tree_map[mypair.level] = mypair.node.data
            if mypair.node.left:
                myqueue.append(Pair(mypair.node.left, mypair.level - 1))
            if mypair.node.right:
                myqueue.append(Pair(mypair.node.right, mypair.level + 1))
        
        for value in tree_map.values():
            print(value, end=" ")


if __name__ == '__main__':
    bt = BinarySearchTree()
    bt.insert(100)
    bt.insert(50)
    bt.insert(200)
    bt.insert(40)
    bt.insert(5)
    bt.insert(60)
    print(bt.nth_largest_element(bt.root, 1))
