from collections import deque

class BFS(object):
    def __init__(self, graph):
        self.graph = graph
        
    def GetEdges(self, start, goal):
        #Create deque object from list = [vertex, [edges]]
        queue = deque([[start, [start]]])
        visited = set()
        while queue:
            vertex, path = queue.popleft()
            #Get next neighbouring vertices
            for next in self.graph[vertex]:
                #Ignore duplicates
                if next not in visited:
                    visited.add(next)
                    if next == goal:
                        yield path + [next]
                    else:
                        queue.append([next, path + [next]])
                
    def GetVertices(self, start):
        queue = deque([start])
        visited = set()
        while queue:
            vertex = queue.popleft()
            #Ignore duplicates
            if vertex not in visited:
                visited.add(vertex)
                if isinstance(self.graph[vertex], set):
                    next = self.graph[vertex]
                else:
                    next = set(self.graph[vertex])
                queue.extend(next-visited)
        return visited
                    
                    
                
            
if __name__ == "__main__":
    graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
    bfs = BFS(graph)
    print(bfs.GetVertices('A'))
    print(list(bfs.GetEdges('A', 'D')))
        
    