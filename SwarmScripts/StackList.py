# Written by Dillon Mead

class StackList:
    size = 0

    def __init__(self):
        self.head = self.tail = None

    def push(self, val):
        if self.head == self.tail == None:
            self.head = Node(val)
            self.tail = self.head
            self.size += 1
        else:
            self.tail.next = Node(val)
            self.tail.next.prev = self.tail
            self.tail.next = self.tail
            self.size += 1

    def pop(self):
        item = self.data
        self.prev.next = None
        self.prev = None
        self.prev = self.tail
        self.size -= 1

        return item
        
    def top(self):
        return self.tail.data

    def getSize(self):
        return self.size

    def display(self):
        cur = self.head
        while cur is not None:
            print(cur.val, end = ' ')
            cur = cur.next
            
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
