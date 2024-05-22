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


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return self.root
        myqueue = queue.SimpleQueue()
        myqueue.put(self.root)
        while not myqueue.empty():
            currentNode = myqueue.get()
            if currentNode.left is not None:
                myqueue.put(currentNode.left)
            if currentNode.right is not None:
                myqueue.put(currentNode.right)
            
            if currentNode.left is None:
                currentNode.left = newNode
                return self.root
            
            if currentNode.right is None:
                currentNode.right = newNode
                return self.root
    
    def zigzagLevelOrder(self, root):
        if root is None: return None
        
        Q = deque()
        Q.append(root)
        flag = True
        
        while Q:
            size = len(Q)
            if flag:
                for i in range(size):
                    node = Q.popleft()
                    print(node.data, end='')
                    if node.left:
                        Q.append(node.left)
                    
                    if node.right:
                        Q.append(node.right)
            else:
                for i in range(size):
                    node = Q.pop()
                    print(node.data, end='')
                    if node.right:
                        Q.appendleft(node.right)
                    if node.left:
                        Q.appendleft(node.left)
            
            flag = not flag
    
    def print_binary_tree(self):
        if self.root is None:
            return
        myqueue = queue.SimpleQueue()
        myqueue.put(self.root)
        while not myqueue.empty():
            currentNode = myqueue.get()
            print(currentNode.data)
            if currentNode.left is not None:
                myqueue.put(currentNode.left)
            if currentNode.right is not None:
                myqueue.put(currentNode.right)
    
    def print_right_side_view(self, root):
        if root is None:
            return
        
        my_queue = deque()
        my_queue.append(Pair(root, 0))
        tree_map = OrderedDict()
        
        while my_queue:
            current_node = my_queue.popleft()
            
            tree_map[current_node.level] = current_node.node.data
            
            if current_node.node.left is not None:
                my_queue.append(Pair(current_node.node.left, current_node.level + 1))
            
            if current_node.node.right is not None:
                my_queue.append(Pair(current_node.node.right, current_node.level + 1))
        
        for key, value in tree_map.items():
            print(key, value)
    
    def print_preorder(self, root):
        if root is None: return
        print(root.data)
        self.print_preorder(root.left)
        self.print_preorder(root.right)
    
    def find_lca(self, root, a, b):
        if root is None: return None
        if root.data == a or root.data == b: return root
        left = self.find_lca(root.left, a, b)
        right = self.find_lca(root.right, a, b)
        
        if left is not None and right is not None: return root
        return left if left is not None else right
    
    def height(self, root):
        if root is None:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)
        
        return 1 + max(left, right)


if __name__ == '__main__':
    bTree = BinaryTree()
    
    bTree.insert(1)
    bTree.insert(2)
    bTree.insert(3)
    bTree.insert(7)
    bTree.insert(6)
    bTree.insert(5)
    bTree.insert(4)
    bTree.zigzagLevelOrder(bTree.root)
