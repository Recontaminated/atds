#!/usr/bin/env python3
"""
unorderedlist_tester.py
This UnorderedList Tester creates an UnorderedList object based
on your class description, and tests to see if it can handle
the common methods.

Your UnorderedList class, and the Node class that it uses, should
be defined in your atds module. In order to assist you in 
debugging any errors, make sure you use the following __repr__
method in your UnorderedList. This will allow you to see what's
happening in your list, and will allow the Tester to provide
better diagnostics for your debugging pleasure. :)

    def __repr__(self):
        '''Creates a representation of the list suitable for 
        printing, debugging.
        ''' 
        return_value = "UnorderedList["
        next_node = self.head
        while next_node != None:
            return_value += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        return_value = return_value + "]"
        return return_value
        
@author Richard White
@version 2023-02-23 (modified)
"""

from atds import *          # Uses the UnorderedList and Node classes
# from unorderedlist_class import *

def main():
    print("Testing the UnorderedList class")
    tests_passed = 0
    try:
        ul = UnorderedList()
        tests_passed += 1
        print("Test passed: UnorderedList object created")
    except:
        print("Test failed: couldn't create UnorderedList object")

    try:
        if ul.is_empty():
            tests_passed += 1
            print("Test passed: .is_empty() method detected empty list")
        else:
            print("Test failed: .is_empty() method didn't understand that list is empty")
    except:
        print("Test failed: .is_empty method unavailable")
    
    try:
        if ul.length() == 0:
            tests_passed += 1
            print("Test passed: .length() correctly identified a length of 0")
        else:
            print("Test failed: .length() didn't identify a length of 0")
    except:
        print("Test failed: .length() method unavailable")
        
    try:
        ul.add(4)
        ul.add(3)
        ul.add(2)
        ul.add(1)
        ul.add(0)
        tests_passed += 1
        print("Test passed: five items added")
    except:
        print("Test failed: couldn't add items")
    

    if not ul.is_empty():
        tests_passed += 1
        print("Test passed: .is_empty() method identified that list is no longer empty")
    else:
        print("Test failed: .is_empty() method thought list was empty, and it isn't")
   
    
    try:
        if ul.length() == 5:
            tests_passed += 1
            print("Test passed: .length() correctly identified a length of 5")
        else:
            print("Test failed: .length() didn't identify a length of 5")
    except:
        print("Test failed: .length() method unusable")
     
    try:
        result = str(ul)         # Try using __repr__
        if result == "UnorderedList[0,1,2,3,4,]":
            tests_passed += 1
            print("Test passed: __repr__ returning correct values:")
            print(result)
        else:
            print("Test failed: __repr__ returned " + result)
            print("Expected: UnorderedList[0,1,2,3,4,]")
        
    except:
        print("Test failed: couldn't reference __repr__ method")

    if not ul.search(5):
        tests_passed += 1
        print("Test passed: .search() method correctly identified that 5 isn't on list")
    else:
        print("Test failed: .search() method thought 5 is on list when it isn't")

        
    try:
        if ul.search(3):
            tests_passed += 1
            print("Test passed: .search() method correctly identified that 3 is on list")
        else:
            print("Test failed: .search() method thought 3 is on list when it isn't")
    except:
        print("Test failed: .search() method unavailable")
    
    try:
        ul.remove(0)
        if str(ul) == "UnorderedList[1,2,3,4,]":
            tests_passed += 1
            print("Test passed: .remove() successfully removed item from beginning of list")
        else:
            print("Test failed: .remove() didn't remove item from beginning of list")
    except:
        print("Test failed: .remove() method unavailable or not working?")

    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.remove(1)
        if str(ul) == "UnorderedList[0,2,]":
            tests_passed += 1
            print("Test passed: .remove() successfully removed item from middle of list")
        else:
            print("Test failed: .remove() didn't remove item from middle of list")
    except:
        print("Test failed: .remove() method unavailable or not working?")
        
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.remove(2)
        if str(ul) == "UnorderedList[0,1,]":
            tests_passed += 1
            print("Test passed: .remove() successfully removed item from end of list")
        else:
            print("Test failed: .remove() didn't remove item from end of list")
    except:
        print("Test failed: .remove() method unavailable or not working?")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.remove(3)
        if str(ul) == "UnorderedList[0,1,2,]":
            tests_passed += 1
            print("Test passed: .remove() successfully didn't remove item from list")
        else:
            print("Test failed: .remove() failed in not removing a non-existent item from list")
    except:
        print("Test failed: .remove() method unavailable or not working?")
    
    try:
        ul = UnorderedList()
        ul.add(0)
        ul.add(1)
        ul.add(0)
        print("Attempting multiple remove")
        print("Before remove: " + str(ul))
        ul.remove(0)
        print("After remove: " + str(ul))
        result = ul.search(0)
        if not result:
            tests_passed += 1
            print("Test passed: .remove() successfully removed multiple items")
        else:
            print("Test failed: .remove() didn't remove multiple items")
    except:
        print("Test failed: .remove() method unavailable or not working?")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.append(3)
        if str(ul) == "UnorderedList[0,1,2,3,]":
            tests_passed += 1
            print("Test passed: .append() successfully appended item to list")
        else:
            print("Test failed: .append() didn't append item to list")
    except:
        print("Test failed: .append() method unavailable or not working?")
    
    try:
        result = ul.index(1)
        if result == 1:
            tests_passed += 1
            print("Test passed: .index() successfully found item on list")
        else:
            print("Test failed: .index() failed to find item on list")
    except:
        print("Test failed: .index() method unavailable? (or __repr__ not working?)")
    

    ul = UnorderedList()
    ul.add(2)
    ul.add(1)
    ul.add(0)
    ul.insert(0, -1)
    if str(ul) == "UnorderedList[-1,0,1,2,]":
        tests_passed += 1
        print("Test passed: .insert() successfully inserted value at beginning of list")
    else:
        print("Test failed: .insert() didn't correctly insert at beginning of list")

    

    ul = UnorderedList()
    ul.add(2)
    ul.add(1)
    ul.add(0)
    ul.insert(2,3)
    if str(ul) == "UnorderedList[0,1,3,2,]":
        tests_passed += 1
        print("Test passed: .insert() successfully inserted values in middle of list")
    else:
        print("Test failed: .insert() didn't correctly insert values in middle of list")

   
    ul = UnorderedList()
    ul.add(2)
    ul.add(1)
    ul.add(0)
    ul.pop()
    if str(ul) == "UnorderedList[0,1,]":
        tests_passed += 1
        print("Test passed: .pop() successfully removed last item from list")
    else:
        print("Test failed: .pop() didn't remove last item from list correctly")


    ul = UnorderedList()
    ul.add(2)
    ul.add(1)
    ul.add(0)
    ul.pop(0)
    if str(ul) == "UnorderedList[1,2,]":
        tests_passed += 1
        print("Test passed: .pop(0) successfully removed first item from list")
    else:
        print("Test failed: .pop(0) didn't remove first item from list correctly")
   
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.pop(1)
        if str(ul) == "UnorderedList[0,2,]":
            tests_passed += 1
            print("Test passed: .pop(1) successfully removed item from middle of list")
        else:
            print("Test failed: .pop(1) didn't remove last item from middle of list correctly")
    except:
        print("Test failed: .pop(1) method unavailable? (or __repr__ not working?)")


        
    print(str(tests_passed) + "/21 tests passed on the UnorderedList class")


if __name__ == "__main__":
    main()