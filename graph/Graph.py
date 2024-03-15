from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)
    
    def addEdge(self, u, v):
        self.adjList[u].append(v)
    
    def bfs(self, startNode):
        my_queue = deque()
        my_set = set()
        my_queue.append(startNode)
        my_set.add(startNode)
        while my_queue:
            currentNode = my_queue.popleft()
            print(currentNode, end=' ')
            for neighbour in self.adjList[currentNode]:
                if neighbour not in my_set:
                    my_set.add(neighbour)
                    my_queue.append(neighbour)
    
    def dfs(self, startNode):
        stack = deque()
        my_set = set()
        stack.append(startNode)
        my_set.add(startNode)
        while stack:
            currentNode = stack.pop()
            print(currentNode, end=' ')
            for neighbour in self.adjList[currentNode]:
                if neighbour not in my_set:
                    my_set.add(neighbour)
                    stack.append(neighbour)
    
    def dfs_util(self, startNode, my_set):
        print(startNode, end=' ')
        my_set.add(startNode)
        for neighbour in self.adjList[startNode]:
            if neighbour not in my_set:
                self.dfs_util(neighbour, my_set)
    
    def dfs_recursion(self, startNode):
        
        my_set = set()
        
        self.dfs_util(startNode, my_set)


if __name__ == '__main__':
    # Add edges to the graph
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    # g.dfs(2)
    
    # Perform BFS traversal starting from vertex 0
    g.dfs_recursion(2)
