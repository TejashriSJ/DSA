# FILO -> First in last out
# we can add data from one end, and we should remove data from the same end
# should assume we can't access the data inbetween ideally, we can do only push,
  # pop and peek (i.e getting the top element without deleting it)
"""
# Uses
# DFS -> in tree traversal, will keep track of noodes to be explored
# browse history -> back button
# Undo action -> text editor
# Recursive function call management
"""

print("Stack Implementation Using Array")

top = -1
stack_size = 5
stack = [None] * stack_size

def push(val):
    global top    
    if top == stack_size -1:
        print("Stack Overflow")
        return
    else:
        top = top + 1
        stack[top] = val
def pop():
    global top 
    if (top == -1):
        print("Stack Underflow")
        return
    else:
        value = stack[top]
        top = top - 1
        return value

def peek():
    return stack[top]
        
def display():
    if top == -1:
        print("Stack is empty")
    else:
        for i in range(top + 1):
            print(stack[i],end = ' ')
        print()
 
def size():
    return top + 1

while(True):
    print(""" 
    Enter your choice
    1: for inserting the element
    2: for deleting the last element
    3: for displaying the elements in stack
    4: for displaying the size of the stack
    5: for peeking the value at the top
    """)
    choice = input()
    if choice == '1':
        val = input("enter the value to push\n")
        push(val)
    elif choice == '2':
        print("The value removed is ",pop())
    elif choice == '3':
        display()
    elif choice == '4':
        print("The size of stack is",size())
    elif choice == '5':
        print("The element at the top is",peek())
    elif choice == '6':
        print("Thank You")
        break
    else:
        print("Enter valid choice")