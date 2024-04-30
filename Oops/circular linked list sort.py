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
            self.tail.next=self.head

    def Sort(self):

        if self.head is None:
            print("Linked List is empty")
        else:
            cur = self.head
            while cur.next.next != self.head.next:
                print(cur.data,end="$$$")
                index = cur.next
                while index != self.head:
                    if cur.data > index.data:
                        cur.data,index.data = index.data,cur.data
                        index = index.next
                cur = cur.next

    def display(self):
        temp=self.head
        while temp.next != self.head:
            print(temp.data)
            temp=temp.next
        print(self.tail.data)

arr=[55,42,13,22,89]
obj=linked_list()
for i in arr:
    obj.append(i)
obj.display()
obj.Sort()
obj.display()