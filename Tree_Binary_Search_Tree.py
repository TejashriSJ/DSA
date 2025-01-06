# Binary Search Tree
# it is a special type of binary tree inn which the nodes which are left to the parent node will always
# less then the root and nodes at right will always be greater than parent node.

#add child, search, in order, pre order, post order traversal

class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if self.data == data:
            print("equal")
            return 
        elif data < self.data:
            print("less")
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTree(data)
        else:
            print("More")
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTree(data)
        
    def search(self,data):
        if self.data == data:
            return True
        elif data < self.data:
            if self.left:
                return self.left.search(data)            
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False
        
    def in_order_traversal(self):
            #in order traversal, display
        elements = []

        #print left
        if self.left:
            elements += self.left.in_order_traversal()
        #print root
        elements.append(self.data)
        print (self.data, end = ',')
        
        #print right
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def Pre_order_traversal(self):
        elements = []
        #root
        print(self.data,end=",")
        elements.append(self.data)
        if self.left:    
            elements += self.left.Pre_order_traversal()    
        if self.right:    
            elements += self.right.Pre_order_traversal()
        return elements
    
    def Post_Order_Traversal(self):
        elements = []

        if self.left:
            elements += self.left.Post_Order_Traversal()
        if self.right:
            elements += self.right.Post_Order_Traversal()
        elements.append(self.data)
        print (self.data, end = ',')

        return elements
        


def CreateTree(listOfData):
    root = BinaryTree(listOfData[0])
    for i in range (1,len(listOfData)):
        root.add_child(listOfData[i])
        
    return root


Tree = CreateTree([10,2,1,5,7,18,25,3])
print("in order",Tree.in_order_traversal()) # sorts elements in ascending order
print("pre order",Tree.Pre_order_traversal())
print("post order",Tree.Post_Order_Traversal())
print("Key found",Tree.search(205))

