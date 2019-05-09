import unittest
from pythonTravis.src.app import addition

class MyTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(1, 1), 2)
        self.assertEqual(addition(1, -1), 0)
        self.assertEqual(addition(0, 0), 0)
        self.assertEqual(addition(-1, -1), -2)
        self.assertEqual(addition(1.0, 1), 2)        
        self.assertEqual(addition(1.1, 1.1), 2.2)
    
if __name__ == '__main__':
    unittest.main()