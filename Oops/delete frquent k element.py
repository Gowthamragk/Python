class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None

    def append(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.temp=node

        else:
            self.temp.next=node
            self.temp=self.temp.next



    def display(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data)
            self.temp=self.temp.next

    def delete_k(self,k):
        if k ==1:
            self.head=None
        else:
            temp=self.head
            cnt=0
            while temp:
                cnt+=1
                temp=temp.next

                ran=cnt//k
                # print(ran)
            temp=self.head
            for i in range(ran):
                count=2
                while count!=k:
                    temp=temp.next
                    count+=1

                if temp.next == None:
                    temp.next=None
                else:
                    temp.next=temp.next.next
                temp=temp.next






obj=linked_list()
arr=[1,2,3,4,5,6,7,8]
for i in arr:
    obj.append(i)
obj.delete_k(8)
obj.display()