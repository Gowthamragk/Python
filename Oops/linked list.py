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


    def display(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data)
            self.temp=self.temp.next

    def insertion_front(self):
        node=Node(data=int(input("Enter the :")))
        node.next=self.head
        self.head=node


    def insertion(self,index):
        new_node=Node(data=int(input("Enter the new")))
        current=self.head
        position=1
        if self.index <position:
            print("invalid index")
        while position != index:
            current=current.next
            position+=1
        if current != None:
            new_node.next=current.next
            current.next=new_node
            
            
def addTwoNumbers(l1, l2):
    carry = 0
    dummy = Node(0)
    current = dummy
    while l1 or l2 or carry:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0
        carry, out = divmod(val1 + val2 + carry, 10)
        current.next = Node(out)
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next


# def mergeTwoLists(l1, l2):
#     # Create a dummy node to serve as the head of the merged list
#     dummy = ListNode(0)
#     current = dummy

#     # Traverse both lists simultaneously
#     while l1 and l2:
#         if l1.val < l2.val:
#             current.next = l1
#             l1 = l1.next
#         else:
#             current.next = l2
#             l2 = l2.next
#         current = current.next

#     # Attach the remaining elements of the non-empty list
#     current.next = l1 if l1 else l2

#     # Return the head of the merged list (excluding the dummy node)
#     return dummy.next


obj1=linked_list()
obj2=linked_list()
obj1.append(3)
obj1.append(2)
obj1.append(4)
obj2.append(2)
obj2.append(1)
obj2.append(3)

merged_list=addTwoNumbers(obj1,obj2)
print(merged_list)
# while merged_list:
#     print(merged_list.val, end=" -> ")
#     merged_list = merged_list.next





# obj1.display()
# #obj1.insertion_front()
# obj1.insertion(3)
# obj1.display()