class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            t=self.head
            while t:
                print(t.data,"->",end=" ")
                t=t.next
L=SinglyLinkedList()
n=Node(10)
L.head=n
n1=Node(20)
L.head.next=n1
n2=Node(30)
L.head.next.next=n2
L.display()
