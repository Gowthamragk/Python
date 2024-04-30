class graph_dict:
    def __init__(self,vertices):
        self.vertices=vertices
        self.dic={}
        
    def add_edge(self,u,v):
        if u not in self.dic:
            self.dic[u]=[v]
        else:
            self.dic[u].append(v)
            
            
    def bfs(self,source):
        visited=set()
        queue=[]
        queue.append(source)
        result=[]
        while len(queue) != 0:
            vertex=queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbour in self.dic[vertex]:
                    if neighbour not in visited:
                        queue.append(neighbour)
        return result
    def find_cyclic(self,start):
        visited = set()
        queue=[start]
        while queue:
            vertex = queue.pop(0)
            if vertex in visited:
                return True
            else:
                visited.add(vertex)
                if vertex in self.dic:
                    for nei in self.dic[vertex]:
                            queue.append(nei)
                        
        return False
    
    
graph=graph_dict(5)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 1)
# graph.add_edge(4, 5)
# graph.add_edge(5, 0)
lst=[0,1,2,3,4]
for i in lst:
    if graph.find_cyclic(i):
        print("Cyclic")
        break
        
else:
    print("Not Cycle")