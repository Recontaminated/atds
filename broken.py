


#! /usr/bin/env python3
"""
  program_name:atds.py 

  description: the module containing all of the data structures used in the advanced topics class
"""
__author__ = "Jeremy "
__version__ = "0.0.1"

from typing import TypeVar,Generic,List,Union
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.stack:List[T] = []
    
    def push(self, item:T) -> None:
        self.stack.append(item) 

    def pop(self) -> Union[T,None]:
        """"
        Instrucutor's directions are to return None if the stack is empty
        """
        if self.stack:
            return self.stack.pop()
        return None
    
    def peek(self) -> Union[T,None]:
        """
        Instrucutor's directions are to return None if the stack is empty
        """

        if self.stack:
            return self.stack[-1]
        else:
            return None
        
    def size (self) -> int:
        return len(self.stack)
    
    def __repr__(self) -> str:
        return repr(self.stack)
    def is_empty(self) -> bool:
        return self.size() == 0
    
    
def test_stack() -> None:
    # stack = Stack() # uncomment this to test the static type checking. Note this will not affect anything at runtime
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.size() == 3
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() == None
    assert stack.size() == 0
    assert stack.peek() == None
    print("Stack tests pass")
if __name__ == "__main__":
    test_stack()


class Queue(Generic[T]):
    def __init__(self):
        self.queue:List[T] = []
    
    def enqueue(self, item:T) -> None:
        self.queue.append(item)
    
    def dequeue(self) -> Union[T,None]:
        if self.queue:
            return self.queue.pop(0)
        return None
    
    def peek(self) -> Union[T,None]:
        if self.queue:
            return self.queue[0]
        return None
    
    def size(self) -> int:
        return len(self.queue)
    
    def is_empty(self) -> bool:
        return self.size() == 0
    
    def __repr__(self) -> str:
        return repr(self.queue)
    def __len__(self) -> int:
        return self.size()
    

class Node(Generic[T]):
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node[data={self.data}, next={self.next}])"
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, data):
        self.data = data
    def set_next(self, next): 
        self.next = next

# class UnorderedList():
    def __init__(self):
        self.head = None
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    def is_empty(self):
        return self.head == None
    def pop(self, index=-1):
        if index == -1:
            index = self.length()-1
        #removes the item at the index from the list and returns it 
        current = self.head
        previous = None
        print(current)
        data = current.get_data()
        self.remove(data)
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()#type:ignore   
        return found
    def remove(self, item):
       # remove all instances of item
        current = self.head
        previous = None

        while current != None:

            if current.get_data() == item:
                if previous == None:
                    self.head = current.get_next()
                    previous = current
                    current = current.get_next()
                else:
                    if current.get_data() == item:
                        previous.set_next(current.get_next())
                        current = current.get_next()
            else:
                previous = current
                current = current.get_next()
        

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count
    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        else:
            current = self.head

            for i in range(pos-1):
                current = current.get_next()
            temp = Node(item)
            temp.set_next(current.get_next())
            current.set_next(temp)

    def append(self, item):
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        temp = Node(item)
        current.set_next(temp)

    def index(self, item):
        current = self.head
        index = 0
        while current != None:
            if current.get_data() == item:
                return index
            else:
                current = current.get_next()
                index += 1
        return None

    def __repr__(self):

        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        if result[-1] == ",":
            result = result[:-1] # remove trailing comma
        result = result + "]"
        return result
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
  
    
class Deque(Generic[T]):
    def __init__(self):
        self.deque:List[T] = []
    
    def add_front(self, item:T) -> None:
        self.deque.insert(0, item)
    
    def add_rear(self, item:T) -> None:
        self.deque.append(item)
    
    def remove_front(self) -> Union[T,None]:
        if self.deque:
            return self.deque.pop(0)
        return None
    
    def remove_rear(self) -> Union[T,None]:
        if self.deque:
            return self.deque.pop()
        return None
    
    def peek_front(self) -> Union[T,None]:
        if self.deque:
            return self.deque[0]
        return None
    
    def peek_rear(self) -> Union[T,None]:
        if self.deque:
            return self.deque[-1]
        return None
    
    def size(self) -> int:
        return len(self.deque)
    
    def is_empty(self) -> bool:
        return self.size() == 0
    
    def __repr__(self) -> str:
        return repr(self.deque)
if __name__ == "__main__":
    n = Node(1)
    print(n)
    n.set_next(Node(2))
    print(n)
    
    print(n)
    test_stack()


class ULStack():
    def __init__(self):
        self.ul = UnorderedList()
    def push(self, item):
        self.ul.add(item)
    def pop(self):
        return self.ul.pop()
    def peek(self):
        data = self.ul.pop()
        self.ul.add(data)
        return data
    def size(self):
        return self.ul.length()
    def is_empty(self):
        return self.ul.is_empty()
    def __repr__(self):
        return self.ul.__repr__()

def test_stack() -> None:
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.size() == 3
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() == None
    assert stack.size() == 0
    assert stack.peek() == None
    print("Stack tests pass")

