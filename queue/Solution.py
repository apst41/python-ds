from queue import PriorityQueue
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        
        pq = PriorityQueue()
        for l in lists:
            if l:
                pq.put(l)
        
        out = ListNode()
        head = out
        while not pq.empty():
            l = pq.get()
            head.next = l
            head = head.next
            if l and l.next:
                pq.put(l.next)
        
        return out.next
    
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if not lists:
    #         return None
    #
    #     pq = PriorityQueue()
    #
    #     # Push the first node of each list into the priority queue
    #     for head in lists:
    #         if head:
    #             pq.put((head.val, head))  # Using a tuple for comparison
    #
    #     dummyNode = ListNode()
    #     current = dummyNode
    #
    #     while not pq.empty():
    #         _, getNode = pq.get()  # Unpacking the tuple to get the node
    #         current.next = getNode
    #         current = current.next
    #         if getNode.next:
    #             pq.put((getNode.next.val, getNode.next))  # Using a tuple for comparison
    #
    #     return dummyNode.next
    
    def print_list(self, root: Optional[ListNode]):
        current = root
        while current:
            print(current.val, end=' ')
            current = current.next


if __name__ == '__main__':
    solution = Solution()
    rootNode = ListNode(1)
    rootNode.next = ListNode(2)
    
    rootNode1 = ListNode(3)
    rootNode1.next = ListNode(4)
    my_list = [rootNode, rootNode1]
    currentrootNode = solution.mergeKLists(my_list)
    solution.print_list(currentrootNode)
