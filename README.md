#Cumulio-Python-SDK

### Python Package

You will need `Python Version >= 3.6`

```console
pip install cumulio
```

### Development Install

You can install cumulio this way if you want to modify the source code. You're going to need [Poetry](https://python-poetry.org/): please refer to the Poetry installation documentation in order to install it.

```console
git clone https://github.com/cumulio/cumulio-sdk-python && cd cumulio-sdk-python
poetry install
```

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
