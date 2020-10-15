import requests
import json

class Cumulio(object):
    def __init__(self, api_key, api_token):
        print("initialized cumulio object")
        if not api_key:
            raise Exception("Please provide a valid API Key")
        if not api_token:
            raise Exception("Please provide a valid API Token")
        self.api_key = api_key
        self.api_token = api_token
        self.APP = "https://app.cumul.io"
        self.HOST = "https://api.cumul.io"
        self.PORT = 443
        self.VERSION = "0.1.0"
    
    def create(self, resource, properties, associations):
        query = {}
        query["action"] = "create"
        query["properties"] = properties
        query["associations"] = associations
        self.__emit(resource, "POST", query)
    
    def __emit(self, resource, action, query):
        query["key"] = self.api_key
        query["token"] = self.api_token
        query["version"] = self.VERSION

        #print(query)
        url = self.HOST + ':' + str(self.PORT) + '/' + self.VERSION + '/' + resource
        x = requests.post(url, headers = {'Content-Type':'application/json'}, data = json.dumps(query))  
        print(x.url)
        print(x.text)