"""
    CS5001_5003 Fall 2023 SV
    HW06
    Xinrui Yi
"""
from collections import deque


class Queue:
    def __init__(self):
        """Constructor
        Parameters:
           self -- the current object
        """
        self.queue = deque()

    def enqueue(self, item):
        """enqueue -- adds something to the end of the queue
        Parameters:
           self -- the current object
           item -- the item to add to the queue
        Returns nothing
        """
        self.queue.append(item)

    def dequeue(self):
        """dequeue -- removes something from the front of the queue
        Parameters:
           self -- the current object
        Returns the element of the front of the queue
        using the deque popleft() method, which is O(1).
        """
        if len(self.queue) == 0:
            raise IndexError("dequeue() called on empty queue")
        else:
            return self.queue.popleft()

    def peek(self):
        """peek -- returns the element at the front of the queue
        Parameters:
           self -- the current object
        Returns the element of the front of the queue
        """
        if len(self.queue) == 0:
            raise IndexError("peek() called on empty queue")
        else:
            return self.queue[0]

    def __str__(self):
        """__str__ -- debugging method for the queue
        Parameters:
           self -- the current object
        """
        return f"{self.queue}"


def main():
    """
    Driver program that uses our queue so that we can see it working
    """
    my_queue = Queue()
    done = False
    while not done:
        cmd = input("enqueue, dequeue, peek, dump or exit (e, d, p, dump or exit)? ")
        if cmd == "e":
            val = input("Data to add? ")
            my_queue.enqueue(val)
        elif cmd == "d":
            val = my_queue.dequeue()
            print("dequeue() returned --", val)
        elif cmd == "p":
            val = my_queue.peek()
            print("peek() returned --", val)
        elif cmd == "dump":
            print(my_queue.__str__())
        elif cmd == "exit":
            done = True


if __name__ == "__main__":
    main()
