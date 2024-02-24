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
L=SinglyLinkedList()
L.display()
