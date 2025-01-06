# delete node
# find min
# find max
# find 2nd min and 2nd max

class Binary_Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_node(self,data):
        if self.data == None:
            self.root = Binary_Tree(data)
        elif self.data == data:
            return
        elif data < self.data:
            
            if self.left:
                self.left.add_node(data)
            else:
                self.left = Binary_Tree(data)
        else:
            if self.right:
                self.right.add_node(data)
            else:
                self.right = Binary_Tree(data)
    def in_order_display(self):
        if self.left:
            self.left.in_order_display()
        print(self.data,end= ",")
        if self.right:
            self.right.in_order_display()
        

        

    def find_min(self):
        if self.left == None:
            return self.data
        return self.left.find_min()
        
    def find_max(self):
        if self.right == None:
            return self.data
        return self.right.find_max()
 
    def find_second_min(self):
        if self.left is None and self.right is None:
            return None
        elif self.left is None:
            return self.right.data
        else:
            parent = 11
            while self.left is not None:
                parent = self.data
                self = self.left
            return parent

    def find_second_max(self):
        if self.left is None and self.right is None:
            return None
        elif self.right is None:
            return self.left.data
        else:
            parent = None
            while self.right is not None:
                parent = self
                self = self.right
            return parent.data

    def delete_node(self,data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete_node(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete_node(data)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.delete_node(min_val)
        return self
    
def Create_Tree(node_list):
    root = Binary_Tree(node_list[0])
    for i in range(1,len(node_list)):
        root.add_node(node_list[i])

    return root

node_list = [101,100,99,105,108,110]
root = Create_Tree(node_list)
root.in_order_display()
print()
root.delete_node(105)
root.in_order_display()  
print()
print("max:",root.find_max())
print("min:",root.find_min())
print("second min:",root.find_second_min())
print("second max:",root.find_second_max())
  


        