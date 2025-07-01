import unittest
from Stack import Stack

class TestStack(unittest.TestCase):
    def test_push_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_peek(self):
        s = Stack()
        s.push('x')
        self.assertEqual(s.peek(), 'x')

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(10)
        self.assertFalse(s.is_empty())

    def test_pop_empty(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()
        
    def test_clear(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.clear()
        self.assertTrue(s.is_empty())


if __name__ == '__main__':
    unittest.main()
