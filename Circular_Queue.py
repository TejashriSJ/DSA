#FIFO
# First in first out or LILO, i.e elements added first should delete first
# standard operations are enqueue, dequeue, peek 

"""
# here time complexity for enqueue and dequeue is O(1), this is better implementation for Normal queue using array.
"""

class queue:
    def __init__(self,size_of_queue):
        self.size = size_of_queue
        self.queue = [None] * size_of_queue
        self.front = -1
        self.rear = -1
        self.count = 0
    def enqueue(self,value):
        if self.isFull():
            print("Overflow")
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
            self.count += 1
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            self.count +=1
            
    def dequeue(self):
        if self.isEmpty():
            print("Underflow")
        elif self.front == self.rear:
            print(f"deleted element is {self.queue[self.front]}")
            self.front = -1
            self.rear = -1
            self.count -= 1
        else:
            print(f"deleted element is {self.queue[self.front]}")
            self.front = (self.front + 1) % self.size
            self.count -=1
            
    def display(self):
        if self.isEmpty():
            print("Underflow") 
        else:
            for i in range(self.front,self.rear + 1):
                print(self.queue[i], end=" ")
            print()

    def peek(self):
        if self.isEmpty():
            return "Underflow"
        else:
            return self.queue[self.front] 

    def get_size(self):
        return self.count  

    def isEmpty(self):
        if self.front == self.rear == -1:
            return True
        return False
    def isFull(self):
        if self.front == (self.rear + 1) % self.size:
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
