import pandas as pd
import requests
from io import StringIO

url = "https://en.wikipedia.org/wiki/Mobile_country_code"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

df = pd.read_html(
    StringIO(html),
    match="Country",
    header=0
)[0]

print(df.head())