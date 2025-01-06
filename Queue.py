#FIFO
# First in first out or LILO, i.e elements added first should delete first
# standard operations are enqueue, dequeue, peek 

"""
# Applications
# Job Scheduling in operating system
# Data buffering
# Breadth first search
"""

class queue:
    def __init__(self,size_of_queue):
        self.size = size_of_queue
        self.queue = [None] * size_of_queue
        self.front = 0
        self.rear = -1
    def enqueue(self,value):
        if self.isFull():
            print("Overflow")
        else:
            self.rear += 1
            self.queue[self.rear] = value
    def dequeue(self):
        if self.isEmpty():
            print("Underflow")
        else:
            print(f"deleted element is {self.queue[self.front]}")
            # shifting elements towards left to fill up the blanks
            # time complexity is O(N), it's a drawback of using array for queue
            # we can use circular queue or linked list for O(1) time compexity
            for i in range(1,self.rear+1):
                self.queue[i-1] = self.queue[i]
            self.rear -= 1
            
    def display(self):
        if self.isEmpty():
            print("Underflow") 
        else:
            for i in range(self.rear+1):
                print(self.queue[i], end=" ")
            print()

    def peek(self):
        if self.isEmpty():
            return "Underflow"
        else:
            return self.queue[self.front]
    def get_size(self):
        return self.rear + 1 

    def isEmpty(self):
        if self.rear == -1:
            return True
        return False
    def isFull(self):
        if self.rear == self.size - 1:
            return True
        return False


queue1 = queue(3)
queue1.enqueue(3)
queue1.enqueue(5)
queue1.enqueue(6)
queue1.enqueue(7)
print("size",queue1.get_size())
queue1.display()
print("peek",queue1.peek())
queue1.dequeue()
queue1.dequeue()
queue1.dequeue()
queue1.dequeue()
print("peek",queue1.peek())
queue1.display()
print("size",queue1.get_size())