from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        if(len(self.container)==0):
            return True
        else:
            return False

    def size(self):
        return len(self.container)

    def print(self):
        print(self.container)

    def print_reverse(string):
        stack =Stack()

        for ch in string:
            stack.push(ch)

        rstr=''
        while stack.size()!=0:
            rstr+=stack.pop()

        return rstr


