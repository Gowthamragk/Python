class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stackll:
    def __init__(self):
        self.head = None
        self.tail = None

    def Push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node

    def Pop(self):
        self.head = self.head.next

    def Peek(self):
        print(self.head.data)

    def Print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


stack = Stackll()
in_li = [10,20,30,40,50]
for i in in_li:
    stack.Push(i)

stack.Push(60)
stack.Push(70)
stack.Pop()
stack.Pop()
stack.Peek()
stack.Print()