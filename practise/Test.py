from sortedcontainers import SortedList


class Node:
    def __init__(self, age, name):
        self.age = age
        self.name = name


if __name__ == '__main__':
    node1 = Node(1, 'ajay')
    node2 = Node(2, 'bjay')
    node3 = Node(3, 'cjay')
    node4 = Node(4, 'djay')
    node5 = Node(5, 'aaaaaejay')
    slist = SortedList(key=lambda node: node.name)
    slist.add(node4)
    slist.add(node5)
    slist.add(node1)
    slist.add(node2)
    slist.add(node3)
    
    for node in slist:
        print(node.age, ' ', node.name, end=' ')
