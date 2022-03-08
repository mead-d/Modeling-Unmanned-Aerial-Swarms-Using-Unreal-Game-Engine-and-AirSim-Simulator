# Written by Dillon Mead


# Singly Linked List
class WaypointList:
    size = 0

    # constructor
    def __init__(self):
        self.head = self.tail = None
        

    # Add new waypoint to tail.
    def addWayPoint(self, coord, speed):
        if (self.head == self.tail == None):
            self.head = Node(coord, speed)
            self.tail = self.head
            self.size += 1
        else:
            self.tail.next = Node(coord, speed)
            self.tail = self.tail.next
            self.size += 1


    # Insert new waypoint between visited nodes and next unvisited node. 
    def insertWayPoint(self, coord, speed):
        cur = self.head
        if (self.head == self.tail == None):
            self.head = Node(coord, speed)
            self.tail = self.head
            self.size += 1
        elif (self.size < 2):
            cur.next = Node(coord,speed)
            self.tail = cur.next
            self.size += 1
        elif (cur.visited == False):
            self.head = Node(coord,speed)
            self.head.next = cur
            self.size += 1
        else:

            # iterate to unvisited waypoint
            while(cur.visited == True):
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

    # Returns first unvisited node
    def validWayPoint(self):
        cur = self.head

        # iterate to unvisited waypoint
        while(cur.visited is not False):
            if(cur.next is not None):
                cur = cur.next
        
        return cur


    # Changes visited flag to True once waypoint is visited.
    def visitWayPoint(self):
        cur = self.head
        
        # iterate to unvisited waypoint
        while(cur.visited is not False):
            if(cur.next is not None):
                cur = cur.next
        
        cur.visited = True

class Node:

    # constructor
    def __init__(self, coord, speed):
        self.coord = coord          # tuple of coordinates
        self.speed = speed          # speed of UAV
        self.visited = False        # If waypoint is already visited
        self.next = None