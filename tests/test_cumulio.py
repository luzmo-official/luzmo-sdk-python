import unittest
from cumulio.cumulio import Cumulio

class TestCumulio(unittest.TestCase):
    key = input("Please enter your Cumul.io API Key: ")
    token = input("Please enter your Cumul.io API Token: ")

    def test_create_dataset(self):
        client = Cumulio(self.key, self.token)
        dataset = client.create("securable", {"type": "dataset", "name" : {"en":"Test Dataset"}})
        self.assertIsNotNone(dataset["id"])
        
    def test_update_description(self):
        client2 = Cumulio(self.key, self.token)
        dataset2 = client2.create("securable", {"type": "dataset", "name" : {"en":"Test Dataset 2"}})
        response = client2.update("securable", dataset2["id"], {"description":{"en":"Description edited"}})
        self.assertEqual(response["description"], {"en":"Description edited"})

    def test_exception_handling(self):
        client3 = Cumulio(self.key, self.token)
        with self.assertRaises(Exception): client3.create("user", {})

if __name__ == '__main__':
    print("testing")
    unittest.main()