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

    def reverse(self,k):
        temp=self.head
        for i in range(k):
            temp=temp.next

        prev=None
        temp2=self.head
        curr=self.head
        nxt=curr.next
        while temp.next!= nxt:
            curr.next=prev
            prev=curr
            curr=nxt
            nxt=nxt.next
        # print(temp2.data)
        # print(curr.data)
        # print(prev.data,end="###")
        self.head=prev
        temp2.next=curr




        # for i in range(k):
        #     curr.next=prev
        #     prev=curr
        #     curr=curr.next
        #     nxt=nxt.next
        # self.head=nxt

        # print(temp1.data)
        # print(temp2.data)
        # temp2.next=temp1.next
        # temp1.next=self.head
        # self.head=temp1

    # def left_rotate(self,k):
    #     temp=self.head
    #     for i in range(k-1):
    #         temp=temp.next
    #     temp2=temp.next
    #     self.tail.next=self.head
    #     self.head=temp2
    #     temp.next=None



    def display(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next


obj=linked_list()
arr=[10,15,12,13,20,14,11,45,12,30]
for i in arr:
    obj.append(i)

# obj.left_rotate(3)
obj.reverse(9)
obj.display()