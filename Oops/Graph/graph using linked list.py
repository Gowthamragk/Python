class Node:
  def __init__(self,vertex=None):
    self.vertex = vertex
    self.next = None
#implementation of linked list for the graph
class LinkedList:
  def __init__(self):
    self.head = None
  
  #add a vertex in the linked list 
  def insert(self, vertex):
    node = Node(vertex) #create a node
    if self.head == None: #if list is empty insert a vertex(node) at the start
      self.head = node
    else:
      temp = self.head
      #iterate through the list till last node is found
      while temp.next: 
          temp = temp.next 
      temp.next = node #adding a new node
  
  #traverse through a linked list
  def traverse(self):
    temp = self.head
    while temp:
      print(temp.vertex, end='-->')
      temp = temp.next
    
#representation of graph using linked lists
class Graph:
  def __init__(self, no_vertices, directed=True):
    self.no_vertices = no_vertices
    self.vertices_list = [LinkedList() for i in range(0, no_vertices)] #create a list to represent the graph
    self.directed = directed 
  
  #insert an edge in the graph
  def insert_edge(self, edge):
    vertex1, vertex2 = edge
    if (vertex1 >=0 and vertex1 < self.no_vertices) and (vertex2 >=0 and vertex2 < self.no_vertices):
      #add an edge from vertex1 to vertex2
      self.vertices_list[vertex1].insert(vertex2)
      if not self.directed: #if the graph is undirected, add an edge from vertex2 to vertex1 as well
        self.vertices_list[vertex2].insert(vertex1)
    else:
      raise ValueError("Invalid vertices")
  
  #display the graph
  def display_graph(self):
    for i in range(0, self.no_vertices):
      print(i, end="\t")
      self.vertices_list[i].traverse()
      print("None")
      
      
n = 5 #number of vertices
graph = Graph(n, directed=False) #create an undirected graph
#insert edges
graph.insert_edge((0, 3)) 
graph.insert_edge((1, 3)) 
graph.insert_edge((1, 2)) 
graph.insert_edge((2, 4)) 
graph.insert_edge((3, 4)) 
#display graph
graph.display_graph()


n = 5 #number of vertices

graph = Graph(n, directed=True) #create a directed graph

#insert edges
graph.insert_edge((0, 3)) 
graph.insert_edge((2, 1)) 
graph.insert_edge((2, 4))
graph.insert_edge((3, 1))  
graph.insert_edge((3, 4)) 
graph.insert_edge((4, 2))

#display graph
graph.display_graph()