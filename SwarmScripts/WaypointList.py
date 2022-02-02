#  Written by Dillon Mead


# Singly Linked List
class WaypointList:
    size = 0

    # constructor
    def __init__(self):
        self.head = self.tail = None

    # Add new waypoint to tail.
    def addWayPoint(coord, speed):
        if (self.head == self.tail == None):
            self.head = Node(coord, speed)
            self.tail = self.head
            self.size += 1
        else:
            self.tail.next = Node(coord, speed)
            self.tail = self.tail.next
            self.size += 1


    # Insert new waypoint between visited nodes and next unvisited node. 
    def insertWayPoint(coord, speed):
        if (self.head == self.tail == None):
            self.head = Node(coord, speed)
            self.tail = self.head
            self.size += 1
        else:
            cur = self.head

            # iterate to unvisited waypoint
            while(cur.visited != False):
                if (cur.next is not None):
                    prev = cur
                    cur = cur.next

            if (cur == self.tail):
                self.tail.next = Node(coord, speed)
                self.tail = self.tail.next
                self.size += 1
            else:
                prev.next = Node(coord, speed)
                prev.next.next = cur
                self.size += 1

    # Changes visited flag to True once waypoint is visited.
    def visitWayPoint():
        cur = self.head
        
        # iterate to unvisited waypoint
        while(cur.visited != False):
            if(cur.next is not None):
                cur = cur.next
        
        cur.visited = True

class Node:

    # constructor
    def __init__(self, coord, speed):
        self.coord = coord
        self.speed = speed
        self.visited = False
        self.next = None
