#Cumulio-Python-SDK

### Python Package

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
