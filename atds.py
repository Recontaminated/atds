


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

class UnorderedList():
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
        for i in range(index):
            current = current.get_next()
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
                    print("removing head")
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
        """Creates a representation of the list suitable for printing,
        debugging.
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
    n.add(Node(3))
    print(n)
  