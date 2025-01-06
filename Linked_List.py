# Linked list is a linear data structure, it's a collection of nodes which are linked to each other.
# Each node contains a data and reference to next node

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def lengthOfList(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count
    
    def display(self):
        if(self.head == None):
            print("List is empty")
        else:
            temp = self.head
            while(temp):
                print(temp.data, end = " ")
                temp = temp.next
            print()

    def insertNodeAtStart(self,data):
        New_Node = node(data)
        print(New_Node.data)

        if self.head == None:
            self.head = New_Node
        else:
            temp = self.head
            self.head = New_Node
            New_Node.next = temp
    
    def insertNodeAtEnd(self,data):
        New_Node = node(data)
        if(self.head == None):
            self.head = New_Node
        else:
            Current_Node = self.head
            Prev_Node = None
            while(Current_Node):
                Prev_Node = Current_Node
                Current_Node = Current_Node.next

            Prev_Node.next = New_Node

    def insertNodeAtIndex(self,data,index):
        if(index >= self.lengthOfList()):
            print("out of range")
        elif index == 0:
            self.insertNodeAtStart(data)
        else:
            count = 0
            current = self.head
            while(count+1 != index and current):
                count += 1
                current = current.next
            New_Node = node(data)
            New_Node.next = current.next
            current.next = New_Node
    
    def deleteNodeAtStart(self):
        if(self.head == None):
            print("Empty")
        else:
           self.head = self.head.next
    
    def deleteNodeAtEnd(self):
        if(self.head == None):
            print("Empty")
        else:
            current_node = self.head
            while(current_node.next.next):
                current_node = current_node.next
            current_node.next = None                
    
    def deleteNodeAtIndex(self,index):
        if(index >= self.lengthOfList()):
            print("out of range")
        elif(index == 0):
            self.deleteNodeAtStart()
        else:
            count = 0
            current_Node = self.head
            while(count+1 < index ):
                count += 1
                current_Node = current_Node.next
            current_Node.next = current_Node.next.next
    
    def updateNode(self,index,data):
        if(index >= self.lengthOfList() or self.head == None):
            print("out of range")
        else:
            count = 0
            current_node = self.head 
            while(count < index):
                current_node = current_node.next
                count += 1
            current_node.data = data
            




L1 = LinkedList()
L1.display()
L1.insertNodeAtStart(10)
L1.insertNodeAtStart(20)
L1.display()
L1.insertNodeAtStart(30)
L1.display()
L1.insertNodeAtEnd(40)
L1.display()
L1.insertNodeAtEnd(50)
L1.display()
L1.insertNodeAtIndex(60,4)
L1.display()
L1.deleteNodeAtStart()
L1.display()
L1.deleteNodeAtEnd()
L1.display()
L1.deleteNodeAtIndex(1)
L1.deleteNodeAtStart()
L1.deleteNodeAtStart()
L1.deleteNodeAtStart()
L1.deleteNodeAtStart()
L1.display()
L1.insertNodeAtEnd(1)
L1.insertNodeAtEnd(2)
L1.insertNodeAtEnd(3)
L1.display()
L1.updateNode(3,25)
L1.display()