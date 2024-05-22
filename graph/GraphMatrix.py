from queue import Queue


class GraphMatrix:
    adj = []
    
    def __init__(self, V):
        self.V = V
        self.adj = [[0 for _ in range(V)] for _ in range(V)]
    
    def addEdge(self, V, E):
        self.adj[V][E] = 1
        self.adj[E][V] = 1
    
    def BFS(self, start):
        seen = set()
        queue = Queue()
        queue.put(start)
        seen.add(start)
        while queue.qsize():
            vis = queue.get()
            print(vis, end=' ')
            for i in range(self.V):
                data = self.adj[vis][i]
                if data not in seen:
                    seen.add(data)
                    queue.put(data)


if __name__ == '__main__':
    g = GraphMatrix(4)
