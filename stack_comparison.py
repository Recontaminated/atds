import time
import random 
from atds import *
import matplotlib.pyplot as plt
import numpy as np

def test_stack_implementation(stack, n=1000):
    """
    Test the implementation of a stack data structure.

    1. Fills the stack with n random data elements using the push
    2. Measures the time taken to fill the stack.
    3. Performs `n` random push, pop, and peek operations on the stack.
    4. Measures the time taken to perform the random operations.

    Note:  we assume that the stack object has the following methods: `push`, `pop`, and `peek`.
    """

    random_data = [random.randint(0, 100) for _ in range(n)]
    time_fill_start = time.time()
    for data in random_data:
        stack.push(data)
    time_fill_end = time.time()

    # random push/pop/peek
    time_fill_start = time.time()
    for _ in range(n):
        stack.push(random.randint(0, 100))
    for _ in range(n):
        stack.pop()
    for _ in range(n):
        stack.peek()
    time_fill_end = time.time()

    return time_fill_end - time_fill_start

def clean_data(data):
    """
    this a work in progress funciton that cleans the data by remving values above the 95th percentile... I realize this is dumb and acually shouldnt work
    """
    values = list(data.values())
    threshold = np.percentile(values, 95)
    cleaned_data = {k: v for k, v in data.items() if v[0] < threshold and v[1] < threshold}
    return cleaned_data
 
def stack_comparison():
    """
    compares the performance of the UnorderedListStack and the Stack class
    """
    plt.figure()
    data = {}
    for i in range(1,100000):
        if i % 100 != 0:
            continue
        print(f"Testing with {i} elements")
        ul_stack = UnorderedListStack()
        ul_stack_time = test_stack_implementation(ul_stack, i)
        sl_stack = Stack()
        sl_stack_time = test_stack_implementation(sl_stack, i)
        data[i] = (ul_stack_time, sl_stack_time)
    plt.plot(data.keys(), [x[0] for x in data.values()], label="UnorderedListStack")
    plt.plot(data.keys(), [x[1] for x in data.values()], label="Stack")
    plt.legend()
    plt.show()



if __name__ == "__main__":
    """main driver function"""
    stack_comparison()