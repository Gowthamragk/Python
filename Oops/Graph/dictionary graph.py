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
            
                
            
    def dfs(self,source):
        visited=set()
        queue=[]
        queue.append(source)
        result=[]
        while queue:
            vertex=queue.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbour in self.dic[vertex]:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        
        return result
        
            
    def display(self):
        # print(self.dic)
        for key,values in self.dic.items():
            # print(i)
            print(key,end="->")
            print(values)
graph=graph_dict(6)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 0)
graph.add_edge(4, 3)
graph.add_edge(4, 5)
graph.add_edge(5, 0)
# graph.add_edge(3, 2)
# graph.add_edge(3, 4)
# graph.add_edge(4, 0)
# graph.add_edge(4, 1)
# graph.add_edge(4, 3)

# while True:
#     try:
#         u=int(input("Enter the node:"))
#         v=int(input("Enter connective node:"))
#         if (u or v) == -1:
#             break
#         else:
#             graph.add_edge(u,v)
#     except:
#         break
# graph.display()
print(graph.bfs(4))
# print(graph.dfs(0))
