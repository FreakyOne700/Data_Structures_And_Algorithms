class Graph:
    def __init__(self,gDict = None):
        if gDict is None:
            gdict = {}
        self.gdict = gDict
    
    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)
    
    def bfs(self,vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop()
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

cDict = {
    "a" : ["b","c"],
    "b" : ["a","d","e"],
    "c" : ["a","e"],
    "d" : ["b","e","f"],
    "e" : ["d","f"],
    "f" : ["d","e"]
}
graph = Graph(cDict)
graph.bfs("a")