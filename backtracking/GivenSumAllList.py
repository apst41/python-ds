from queue import PriorityQueue
from typing import List


class Node:
    def __init__(self, value, count):
        self.value = value
        self.count = count


class Solution:
    setattr(Node, "__lt__", lambda self, other: self.count <= other.count)
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = {}
        pq = PriorityQueue()
        
        for i in nums:
            hash_map[i] = 1 + hash_map.get(i, 0)
        
        for v, c in hash_map.items():
            
            if pq.qsize() < k:
                pq.put(Node(v, c))
            
            else:
                if pq.queue[0].count < c:
                    pq.get()
                    pq.put(Node(v, c))
        
        ans = []
        
        while pq.qsize():
            ans.append(pq.get().count)
        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]
    
    my = sol.topKFrequent(arr, 2)
    for i in my:
        print(i)
