#!/usr/bin/env python3
"""
atds.py
The module containing all of the data structures used in the
Advanced Topics in CS course at Poly.
"""
__author__ = "Richard White"
__version__ = "2024-02-13"


class Stack(object):
    """Describes a Stack that can be used with push
    and pop commands.
    """
    def __init__(self):
        self.st = []

    def push(self, item):
        self.st.append(item)

    def pop(self):
        if len(self.st) > 0:
            return self.st.pop()
        else:
            return None
    
    def peek(self):
        """Returns the item on the "top" of
        the list, as long as there's an item there.
        """
        if len(self.st) > 0:
            return self.st[-1]
        else:
            return None

    def size(self):
        return len(self.st)
    
    def is_empty(self):
        return len(self.st) == 0
    
    def __repr__(self):
        return str(self.st)
    
class Queue(object):
    """Describes a queue that can be used with enqueue
    and dequeue methods.
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def __repr__(self):
        return str(self.queue)

class Deque(object):
    """Describes a double-ended queue, with index 0
    the "front" of the Deque and index -1 at the rear.
    """

    def __init__(self):
        self.deque = []
    
    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        return self.deque.pop(0)
    
    def remove_rear(self):
        return self.deque.pop()
    
    def size(self):
        return len(self.deque)
    
    def is_empty(self):
        return len(self.deque) == 0

class Node(object):
    """Defines a node class to be used in an
    UnorderedList, coming soon.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
    def set_data(self, data):
        self.data = data
    def get_data(self):
        return self.data
    def set_next(self, next):
        self.next = next
    def get_next(self):
        return self.next
    def __repr__(self):
        return "Node[data=" + str(self.data) + ",next=" + str(self.next) + "]"

class UnorderedList(object):
    """Defines an unordered (unsorted) list of nodes.
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, data):
        """Inserts a new node at the beginning of
        the list
        """
        temp_node = Node(data)
        temp_node.set_next(self.head)
        self.head = temp_node

    def length(self):
        """Identifies the length of the list by
        going through the entire list. Painful!
        """
        node_count = 0
        current = self.head
        while current != None:
            current = current.get_next()
            node_count += 1
        return node_count 

    def search(self, data):
        """Returns True if the data is on the list.
        """
        current = self.head
        found = False
        while current != None and not found: 
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, data):
        """Removes multiple occurrences of data on the list, 
        which requires going through the entire list until
        you hit the end, or nothing if the data isn't on the list.
        """
        current = self.head
        previous = None
        while current != None and self.head != None:    # Have to search entire list
            if current.get_data() == data:              # need to remove it
                if previous == None:                    # we're at the head
                    self.head = current.get_next()
                    current = current.get_next()
                else:
                    previous.set_next(current.get_next())
                    current = current.get_next()
            else:                                       # pass on through
                previous = current
                current = current.get_next()

    def append(self, data):
        """Appends an item to the end of the list
        """
        temp = Node(data) 
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(temp)

    def index(self, data):
        """Returns the index of the first occurence of the data
        in the list.
        """
        if self.head == None:
            return None
        current = self.head
        index = 0
        while current != None and current.get_data() != data:
            current = current.get_next()
            index += 1
        if current == None:
            return None
        else:
            return index

    def insert(self, position, data):
        """Inserts the piece of data at the indicated position.
        """
        temp = Node(data)
        index = 0
        current = self.head
        previous = None
        while index < position:
            previous = current
            current = current.get_next()
            index += 1
        if index == 0:
            temp.set_next(current)
            self.head = temp
        else:
            previous.set_next(temp)
            temp.set_next(current)
            
    def pop(self, index=-1):
        """Removes item at position index, or at the end of the list
        (-1) if no index is indicated.
        """
        if self.head == None:
            return None      # Can't pop from empty list
        if index == -1:
            current = self.head
            previous = None
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            result = current.get_data()
            previous.set_next(None)
            return result
        elif index == 0:
            current = self.head
            result = current.get_data()
            self.head = current.get_next()
            return result
        else:       # returning from middle of list?
            current = self.head
            previous = None
            position = 0
            while position < index:
                previous = current
                current = current.get_next()
                position += 1
            result = current.get_data()
            previous.set_next(current.get_next())
            return result

    def __repr__(self):
        """Creates a representation of the list suitable for printing, debugging.
        """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result

class UnorderedListStack(object):
    """Implements a Stack using the UnorderedList class.
    """
    def __init__(self):
        self.ul = UnorderedList()

    def push(self, item):
        """Pushes an item onto the top of the stack"""
        self.ul.add(item)

    def pop(self):
        """Removes the item at the top of the stack and
        returns it.
        """
        return self.ul.pop(0)
    
    def peek(self):
        """Examines the item at the top of the stack
        and returns that value. Awkward: we don't have
        a way to look at data at the beginning of an
        Unordered List!"""
        value = self.ul.pop(0)
        self.ul.add(value)
        return value

    def size(self):
        return self.ul.length()

    def is_empty(self):
        return self.ul.is_empty()
    
def main():
    pass

if __name__ == "__main__":
    main()


class HashTable(object):
    def __init__(self, size) -> None:
        self.slots = [None for i in range(size)]
        self.data = [None for i in range(size)]

    def __repr__(self) -> str:
        return f"{self.data} | {self.slots}"
        
    def hash_function(self,key):
        return key % len(self.slots)
    
    def transform_put_index(self,index):
        """manages hash colisions"""
        if self.data[index] == None:
            return index
        return self.transform_put_index(index+1)
    
    def transform_get_index(self,index,key):
        while self.slots[index]!= key:
            if self.slots[index] == None:
                return -1
            index +=1
        return index
    
    def put(self, key,value):
        index = self.hash_function(key)
        index = self.transform_put_index(index)
        self.slots[index] = key
        self.data[index] = value
    def get(self,key):
        index = self.hash_function(key)
        index = self.transform_get_index(index,key)
        if index == -1:
            return None
        return self.data[index]
    # def remove(self,index):
    #     index = self.hash_function(key)
        

 


import typing
import typing

class BinaryTree(object):
    def __init__(self, key):
        self.children = [None, None]
        self.value = key

    def get_root_val(self):
        return self.value

    def set_root_val(self, new_val):
        self.value = new_val

    def get_left_child(self):
        return self.children[0]

    def get_right_child(self):
        return self.children[1]

    def insert_left(self, new_left_child):
        if self.children[0] is None:
            self.children[0] = BinaryTree(new_left_child)
        else:
            new_child = BinaryTree(new_left_child)
            new_child.children[0] = self.children[0]
            self.children[0] = new_child

    def insert_right(self, new_right_child):
        if self.children[1] is None:
            self.children[1] = BinaryTree(new_right_child)
        else:
            new_child = BinaryTree(new_right_child)
            new_child.children[1] = self.children[1]
            self.children[1] = new_child

    def __str__(self):
        return f"BinaryTree[key={self.value},left_child={self.children[0]},right_child={self.children[1]}]"

    def __repr__(self):
        return f"BinaryTree[key={self.value},left_child={self.children[0]},right_child={self.children[1]}]"



class Vertex(object):
    """Describes a vertex object in terms of a "key" and a
    dictionary that indicates edges to neighboring vertices with
    a specified weight.
    """
    
    def __init__(self, key):
        """Constructs a vertex with a key value and an empty dictionary 
        in which we'll store other vertices to which this vertex is
        connected.
        """
        self.id = key
        self.connected_to = {}   # empty dictionary for neighboring vertices
        self.color = 'white'
        self.distance = 0
        self.predecessor = None
        self.discovery_time = 0     # discovery time
        self.finish_time = 0        # finish time  
    
    def add_neighbor(self, neighbor_vertex, weight=0):
        """Adds a reference to a neighboring Vertex object to the
        dictionary, to which this vertex is connected by an edge. 
        If a weight is not indicated, default weight is 0.
        """
        self.connected_to[neighbor_vertex] = weight
    
    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_distance(self, distance):
        self.distance = distance
    
    def get_distance(self):
        return self.distance
    
    def set_predecessor(self, predecessor):
        self.predecessor = predecessor
    
    def get_predecessor(self):
        return self.predecessor
    
    def set_discovery(self, discovery_time):
        self.discovery_time = discovery_time
    
    def get_discovery(self):
        return self.discovery_time
    
    def set_finish(self, finish_time):
        self.finish_time = finish_time
    
    def get_finish(self):
        return self.finish_time
    
    def __repr__(self):
        """Returns a representation of the vertex and its neighbors,
        suitable for printing. Check out the example of 'list
        comprehension' here!
        """
        return 'Vertex[id=' + str(self.id) \
                + ',color=' + self.color \
                + ',dist=' + str(self.distance) \
                + ',pred=' + str(self.predecessor) \
                + ',disc=' + str(self.discovery_time) \
                + ',fin=' + str(self.finish_time) \
              + '] connected_to: ' + str([x.id for x in self.connected_to]) 
    
    def get_connections(self):
        """Returns the keys of the vertices we're connected to
        """
        return self.connected_to.keys()
    
    def get_id(self):
        """Returns the id ("key") for this vertex
        """
        return self.id
    
    def get_weight(self, neighbor_vertex):
        """Returns the weight of an edge connecting this vertex 
        with another.
        """
        return self.connected_to[neighbor_vertex]

class Graph:
    def __init__(self) -> None:
        
        self.graph = {}
    def add_edge(self, from_vertex, to_vertex, weight=0):
        if from_vertex not in self.graph:
            self.add_vertex(from_vertex)
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)
        self.graph[from_vertex].add_neighbor(self.graph[to_vertex], weight)
    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.graph[key] = new_vertex
        return new_vertex
    def get_vertex(self, key):
        return self.graph.get(key)
    def __contains__(self, key):
        return key in self.graph
    def __iter__(self):
        return iter(self.graph.values())

    

