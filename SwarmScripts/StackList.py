# Written by Dillon Mead

# Doubly linked list implemented as stack. Top of stack is list tail
class StackList:
    size = 0

    # constructor
    def __init__(self):
        self.head = self.tail = None

    # adds node with input as value to tail. increments size by one
    def push(self, val):
        if self.head == self.tail == None:
            self.head = Node(val)
            self.tail = self.head
            self.size += 1
        else:
            self.tail.next = Node(val)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.size += 1

    # removes top(tail) of stack. decrements size by one
    def pop(self):
        item = self.data
        self.prev.next = None
        self.prev = None
        self.prev = self.tail
        self.size -= 1

        return item
    
    # returns the value of the top node
    def top(self):
        return self.tail.data

    # returns the recorded size
    def getSize(self):
        return self.size

    # prints stack from head to tail
    def display(self):
        cur = self.head
        while cur is not None:
            print(cur.val, end = ' ')
            cur = cur.next
            

class Node:
    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
