# BFS -> breadth first search
class Binary_Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.queue = []
      

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
    def BFS(self):
        self.queue.append(self)
        i = 0
        while i < len(self.queue):
            node = self.queue[i]
            print(node.data,end = ",")    
            if node.left:
                self.queue.append(node.left)
            if node.right:
                self.queue.append(node.right)
            i += 1
    
def Create_Tree(node_list):
    root = Binary_Tree(node_list[0])
    for i in range(1,len(node_list)):
        root.add_node(node_list[i])

    return root

node_list = [4,3,2,1,5,6,7,8]
root = Create_Tree(node_list)        
root.in_order_display()
print()
root.BFS()        