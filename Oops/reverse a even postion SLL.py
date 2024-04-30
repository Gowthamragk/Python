class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Single:
    def __init__(self):
        self.head = None
        self.time = 0
        self.lis = []
    def create(self,data):
        self.time += 1
        newNode = Node(x)
        if self.head == None:
            self.head = newNode
            self.temp = newNode
        else:
            self.temp.next = newNode
            self.temp = self.temp.next
    def display(self):
        self.temp = self.head
        while self.temp:
            print(self.temp.data,end=" ")
            self.temp = self.temp.next
    def even(self):
        self.temp = self.head
        if self.time > 3:
            pos = 0
            while self.temp.next:
                pos += 1
                self.pre = self.temp
                self.temp = self.temp.next
                if pos%2 != 0:
                    self.lis.append(self.temp.data)
                    self.pre.next = self.temp.next
                    self.temp = self.pre
            self.insert()
        else:
            self.display()
    def insert(self):
        self.temp = self.head
        self.lis.reverse()
        for x in range(len(self.lis)):
            newNode = Node(self.lis[x])
            self.next1 = self.temp.next
            self.temp.next = newNode
            self.temp = self.temp.next
            self.temp.next = self.next1
            self.temp = self.temp.next
a = Single()
for x in range(1,10):
    a.create(data=x)
a.even()
# a.insert()
a.display()