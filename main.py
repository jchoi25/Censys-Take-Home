from censys.search import CensysCertificates
from pandas import DataFrame
from pathlib import Path

c = CensysCertificates()

fields = [
    "parsed.fingerprint_sha256",
    "parsed.validity.start",
    "parsed.validity.end",
]

df = DataFrame(
    c.search("parsed.names: censys.io and tags: trusted", fields))
filepath = Path('./out.csv')

df.to_csv(filepath, index=False, columns=fields)
