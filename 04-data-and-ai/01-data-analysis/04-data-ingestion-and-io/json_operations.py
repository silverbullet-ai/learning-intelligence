import pandas as pd
from io import StringIO

data = """
[
    {
        "name":"Aahish",
        "age":24
    }
]
"""

df = pd.read_json(StringIO(data))

print(df)

print(df.to_json())