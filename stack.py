# author: Jaisuraj Kaleeswaran
# date: March 6, 2023
# file: stack.py makes a Stack class
# input: Input data inserted into the stack
# output: Output data popped from the stack

class Stack:  # a class that creates a stack
    def __init__(self, items = []):
        self.items = items #Initialize items to be equal to self.items

    def isEmpty(self): #Returns a boolean value to indicate whether self.items is empty or not
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self): 
        if not self.isEmpty(): #If self.items is not empty 
            return self.items[len(self.items) - 1] #Return the last element in the list
        return None   #Return none of self.items is empty
    
    def size(self):
        return len(self.items)

# a driver program for class Stack
if __name__ == '__main__':

    #A list is created in order to be implemented in a stack
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i) #Each element in the list is being pushed to the stack

    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]

    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())

    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None
    print("All tests passed!")