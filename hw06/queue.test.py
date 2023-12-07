from queue_as_dequeue import Queue
import unittest
from collections import deque


class QueueTest(unittest.TestCase):
    # Test enqueue, peek, dequeue and str
    def test_enqueue(self):
        my_queue = Queue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        self.assertEqual(my_queue.peek(), 1)
        self.assertEqual(my_queue.dequeue(), 1)
        str_p = my_queue.__str__()
        self.assertEqual(str_p, "deque([2, 3])")

    # Test enqueue and dequeue
    def test_dequeue(self):
        my_queue = Queue()
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        my_queue.enqueue(4)
        self.assertEqual(my_queue.dequeue(), 2)

    # Test enqueue, dequeue, and peek
    def test_peek(self):
        my_queue = Queue()
        my_queue.enqueue(3)
        my_queue.enqueue(4)
        my_queue.enqueue(5)
        self.assertEqual(my_queue.peek(), 3)
        str_p = my_queue.__str__()
        self.assertEqual(str_p, "deque([3, 4, 5])")

    # Test str
    def test_str(self):
        my_queue = Queue()
        my_queue.enqueue(4)
        my_queue.enqueue(5)
        my_queue.enqueue(6)
        str_p = my_queue.__str__()
        self.assertEqual(str_p, "deque([4, 5, 6])")

    # Test empty queue dequeue
    def test_dequeue_empty(self):
        empty_queue = Queue()
        with self.assertRaises(IndexError):
            empty_queue.dequeue()

    # Test empty queue peek
    def test_peek_empty(self):
        empty_queue = Queue()
        with self.assertRaises(IndexError):
            empty_queue.peek()


def main():
    unittest.main(verbosity=3)


main()
