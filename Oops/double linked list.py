# double linked list
class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head =None
        self.tail=None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head =new_node
            self.tail=new_node
        else:
            self.tail.next = new_node
            new_node.prev=self.tail
            self.tail=new_node
    def display(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data)
            self.temp=self.temp.next


    def add_two(self,k):
        temp=self.head
        while temp:
            temp2=temp.next
            while temp2:
                if temp.data+temp2.data==k:
                    print(temp.data,end=" ")
                    print(temp2.data,end=" ")
                    print()
                temp2=temp2.next
            temp=temp.next


    def insertion_front(self):
        front=Node(int(input("Enter the front value")))
        self.head.prev=front
        front.next=self.head
        self.head=front


obj1=DoubleLinkedList()
arr=[1,2,3,4,5,6]
for i in arr:
    obj1.append(i)
# obj1.append()
# obj1.append()
# obj1.display()
# obj1.insertion_front()
# obj1.display()

obj1.add_two(6)

