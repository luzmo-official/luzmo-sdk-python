#Cumulio-Python-SDK

### Python Package

You will need `Python Version >= 3.6`

```console
pip install cumulio
```

### Documentation

For detailed documentation, please visit the [Cumul.io Developer Docs](https://developer.cumul.io/)

### Usage and Examples

Create a Cumul.io dataset:

```console
from cumulio.cumulio import Cumulio

key = "Your Cumul.io key"
token = "Your Cumul.io token"

client = Cumulio(key, token)
dataset = client.create("securable", {"type": "dataset", "name" : {"en":"Example with python sdk"}})
client.update("securable", dataset[" "], {"description":{"en":"This is an example description"}})
```

Optionally for people working with VPC or on our US multitenant environment, you can also define an api_host while creating the client. If not it will default to "https://api.cumul.io"

E.g.:

```console
client = Cumulio(key, token, "https://api.us.cumul.io")
```

There is also the option of adding a dictionary of proxies while creating the API client.

Update description of dataset:

```console
client.update("securable", dataset["id"], {"description":{"en":"Joost edited"}})
```

Create a column in the dataset:

```console
burrito_column = client.create('column', { "type": 'hierarchy', "format": '',"informat": 'hierarchy', "order": 0,"name": {"nl": 'Type burrito'}})
client.associate("securable", dataset["id"], "Columns", burrito_column["id"])
```

Add Values to the column:

```console
client.create("data", dataset["id"], {"securable_id": dataset["id"],"type": "append", "data": [["sweet"], ["sour"]]})
```

Replace Values in the column:

```console
client.create("data", {"securable_id": dataset["id"],"type": "replace", "data": [["bitter"], ["salty"]]})
```

### Documentation

The API documentation (available services and methods) can be found at https://developer.cumul.io
