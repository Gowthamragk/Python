#swap the node in the single linkedlist without swap the data #10 15 12 13 20 14

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None

    def append(self):
        node=Node(data=int(input("Enter the :")))
        if self.head is None:
            self.head=node
            self.temp=node

        else:
            self.temp.next=node
            self.temp=self.temp.next


    def swap(self,x,y):
        temp=self.head
        while temp.data!=x and temp.next.data!=x:
            temp=temp.next

        temp2=self.head
        while temp2.next.data!=y:
            temp2=temp2.next
        # res1=temp2.next
        # res2=temp.next
        # res4=temp2.next.next
        # res=temp.next.next
        # temp.next=temp2.next
        # # print(temp2.next.data,end="#")
        # temp2.next.next=res
        # temp2.next=res2
        # temp.next.next=res4

        if temp.data ==x:
            temp=self.head
            res=temp2.next
            temp.next,temp2.next.next=temp2.next.next,temp.next
            temp2.next=temp
            self.head=res
            # print(self.head.data,end="#")
            # print(temp2.next.data,end="#")
        else:
            temp.next.next,temp2.next.next=temp2.next.next,temp.next.next
            temp.next,temp2.next=temp2.next,temp.next





        # res=temp.next
        # temp.next=temp2.next
        # temp2.next=res

        # print(temp2.data,end="%")
        # print(temp.data,end="%")

    def display(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data)
            self.temp=self.temp.next



obj1=linked_list()
obj1.append()
obj1.append()
obj1.append()
obj1.append()
obj1.append()
obj1.append()

obj1.swap(1,3)
obj1.display()