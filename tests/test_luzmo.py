import unittest
from luzmo.luzmo import Luzmo

class TestLuzmo(unittest.TestCase):
    key = input("Please enter your Luzmo API Key: ")
    token = input("Please enter your Luzmo API Token: ")

    def test_create_dataset(self):
        client = Luzmo(self.key, self.token)
        dataset = client.create("securable", 
        {
            "type": "dataset", 
            "name" : {"en":"Test Dataset"}
        })
        self.assertIsNotNone(dataset["id"])
        
    def test_update_description(self):
        client2 = Luzmo(self.key, self.token)
        dataset2 = client2.create("securable", {"type": "dataset", "name" : {"en":"Test Dataset 2"}})
        response = client2.update("securable", dataset2["id"], {"description":{"en":"Description edited"}})
        self.assertEqual(response["description"], {"en":"Description edited"})
    
    def test_column_creation(self):
        client3 = Luzmo(self.key, self.token)
        dataset3= client3.create("securable", {"type": "dataset", "name" : {"en":"Test Dataset 3"}})
        client3.create("column", 
        {
            "type": 'hierarchy',
            "format": '',
            "informat": 'hierarchy',
            "order": 0,
            "name": {"nl": 'Type burrito'}
        }, 
        [{
            "role": "securable", 
            "id": dataset3["id"]
        }])

    def test_exception_handling(self):
        client3 = Luzmo(self.key, self.token)
        with self.assertRaises(Exception): client3.create("user", {})

if __name__ == '__main__':
    print("testing")
    unittest.main()