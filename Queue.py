from collections import deque

class Queue:
    def __init__(self):
        self.buffer=deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)
        return

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        if len(self.buffer)==0:
            return True
        else:
            return  False

    def size(self):
        return len(self.buffer)

    def print_queue(self):
        for i in self.buffer:
            self.buffer.pop()


que_1 = Queue()
que_1.enqueue([45,55,85,96,321])