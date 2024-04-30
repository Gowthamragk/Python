class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[0]*self.vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adjacency_list[u][v]=1
        self.adjacency_list[v][u]=1
        
    def display(self):
        for i in self.adjacency_list:
            print(self.adjacency_list)

    # def print_graph(self):
    #     for vertex in range(self.vertices):
    #         print("Adjacency list of vertex", vertex)
    #         print("head", end="")
    #         for neighbor in self.adjacency_list[vertex]:
    #             print(" ->", neighbor, end="")
    #         print(" \n")


# E/xample usage:

num_vertices = 5
graph = Graph(num_vertices)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
# graph.print_graph()
graph.display()

