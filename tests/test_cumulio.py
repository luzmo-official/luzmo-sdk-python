import unittest
from cumulio.cumulio import Cumulio

class TestCumulio(unittest.TestCase):
    def test_dummy(self):
        client = Cumulio(0,2)
        print(client)
        print("here")
        #self.assertRaises .assertEqual(1, 2)
    
    def test_dummy2(self):
        self.assertEqual(2, 2)

if __name__ == '__main__':
    print("testing")
    unittest.main()