class Cumulio(object):
    def __init__(self, api_key, api_token):
        self.api_key = api_key
        self.api_token = api_token
        self.APP =  "https://app.cumul.io"
        self.HOST = "https://api.cumul.io"
        self.PORT = 443
        self.VERSION = "0.1.0"
    
    def create(self, resource, properties, associations):
        query = {}
        query["action"] = "create"
        query["properties"] = properties
        query["assocoations"] = associations
        self.__emit(resource, "POST", query)
    
    def __emit(self, resource, action, query):
        print("about to emit")