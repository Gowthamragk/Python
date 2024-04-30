class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.tail=node

        else:
            self.tail.next=node
            self.tail=node


    def left_rotate(self,k):
        temp=self.head
        for i in range(k-1):
            temp=temp.next
        temp2=temp.next
        self.tail.next=self.head
        self.head=temp2
        temp.next=None



    def display(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next


obj=linked_list()
arr=[1,5,3,4,2]
for i in arr:
    obj.append(i)

obj.left_rotate(3)
obj.display()