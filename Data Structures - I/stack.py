'''
Stack:
    - Pile of books kept on top of each other
    - Last In First Out (LIFO) Data structure

    - Operations:
        - Push: Inserting element in Stack
        - Pop: Deletion of element from Stack
        - isEmpty: Check if the Stack is Empty
        - isFull: Check if the Stack is Full
        - Peek: Get the value of top element without removing it

    - States:
        - Empty Stack: No elements present in Stack
        - Underflow: Pop operation on Empty Stack
        - Partially Filled Stack: Stack with number of elements less than it's capacity
        - Completely Filled Stack: Stack with number of elements equal to it's capacity
        - Overflow: Push operation on Completely Filled Stack

    - Space Complexity:
        - O(n): For storing 'n' elements at same time
        - O(1): For storing 'n' elements with continuous Push & Pop Operations
    - Time Complexity:
        - O(1)
'''

class stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.top = -1

    def isEmpty(self):
        '''
        :return: True if Stack is Empty; Otherwise False
        '''
        return True if self.top == -1 else False

    def isFull(self):
        '''
        :return: True if Stack is Full; Otherwise False
        '''
        return True if self.top == self.capacity - 1 else False

    def push(self, item):
        '''
        :param item: element to be push
        :return: If Stack is not full, Top, Updated Stack
        '''
        if self.isFull() == True:
            return 'Stack is Full Push Operation Failed !!!'
        else:
            self.top += 1
            self.items.append(item)
            return 'Top: {}; Stack: {}'.format(stack.top, stack.items)

    def pop(self):
        '''
        :return: If Stack is not empty, Popped Element, Top & Updated Stack
        '''
        if self.isEmpty() == True:
            return 'Stack is Empty Pop Operation Failed !!!'
        else:
            self.top -= 1
            temp = self.items.pop()
            return 'Popped: {}; Top: {}; Stack: {}'.format(temp, stack.top, stack.items)

    def peek(self):
        '''
        :return: Last element in Stack
        '''
        return 'Last element in Stack is: {}'.format(self.items[-1])


if __name__ == '__main__':
    capacity = 5
    stack = stack(capacity=5)
    print('Empty Stack Creation')
    print('Stack capacity: {}'.format(stack.capacity))
    print('Top: {}; Stack: {}'.format(stack.top, stack.items))
    print('Is stack Empty: {}'.format(stack.isEmpty()))
    print('Is stack Full: {}\n'.format(stack.isFull()))

    print('Push Operation')
    print(stack.push(12))
    print(stack.push(34))
    print(stack.push(45))
    print(stack.push(2))
    print(stack.push(30))
    print('Is stack Full: {}\n'.format(stack.isFull()))
    print('Overflow')
    print(stack.push(3))

    print('\nPop Operation')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print('Is stack Empty: {}\n'.format(stack.isEmpty()))
    print('Underflow')
    print(stack.pop())

    print('\nPeek')
    print(stack.push(12))
    print(stack.push(34))
    print(stack.push(45))
    print(stack.peek())