from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
    
    def reverse_list(self, root):
        if root.next is None or root is None: return root
        newHead = self.reverse_list(root.next)
        root.next.next = root
        root.next = None
        self.head = newHead
        return self.head
    
    def delete_nth_element_from_end(self, root, n):
        if root is None: return root
        
        dummy_node = Node(12345)
        dummy_node.next = root
        
        slow = dummy_node
        fast = dummy_node
        
        for i in range(0, n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
        return self.head
    
    def hasCycle(self, head: Optional[Node]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        
        return False
    
    def reverse_in_group(self, root, k):
        if root is None: return root
        
        current = root
        prev = None
        count = 0
        my_next = None
        
        while current and count < k:
            my_next = current.next
            current.next = prev
            prev = current
            current = my_next
            count += 1
        
        if my_next:
            root.next = self.reverse_in_group(my_next, k)
        
        self.head = prev
        return self.head
    
    def find_intersection_of_list(self, nodeA, nodeB):
        if not nodeA and not nodeB:
            return nodeA
        
        my_set = set()
        
        currentA = nodeA
        currentB = nodeB
        
        while currentA:
            my_set.add(currentA)
            currentA = currentA.next
        while currentB:
            if currentB not in my_set:
                my_set.add(currentB)
                currentB = currentB.next
            
            else:
                return currentB
        
        return None
    
    def rotatedList(self, node, k):
        if not node:
            return node
        
        prev = next = None
        current = node
        count = 0
        
        while current and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        
        if current:
            node.next = self.rotatedList(next, k)
        
        self.head = prev
        
        return self.head


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.head = Node(1)
    linked_list.head.next = Node(2)
    linked_list.head.next.next = Node(3)
    linked_list.head.next.next.next = Node(4)
    linked_list.head.next.next.next.next = Node(5)
    
    new_linked_list = LinkedList()
    
    new_linked_list.head = linked_list.head.next.next
    linked_list.print_list()
    
    print()
    
    linked_list.rotatedList(linked_list.head, 2)
    linked_list.print_list()
