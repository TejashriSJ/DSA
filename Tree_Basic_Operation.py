# Root Node
    # Node -> (Parent Node or Child Node or Leaf Node)

class Tree:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    def display(self):
        if(self.parent):
           print(" " * self.get_level() * 3 +"|--" + self.data)

        for child in self.children:
            child.display();

    def get_level(self):
        level = 0
        parent = self.parent
        while(parent):
            level += 1
            parent = parent.parent
        return level    
   
    
Root = Tree("Electronics")
print(Root.data)
Child1 = Tree("Mobile")
Child2 = Tree("TV")
Child3 = Tree("Speakers")

Root.add_child(Child1)
Root.add_child(Child2)
Root.add_child(Child3)

Child1.add_child(Tree("Samsung"))
Child1.add_child(Tree("IPhone"))

Child2.add_child(Tree("Sony"))
Child2.add_child(Tree("LG"))

Child3.add_child(Tree("Bose"))

print(Root.get_level())
print(Child3.get_level())
print(Child3.children[0].get_level())

Root.display()
