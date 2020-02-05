import pandas as pd

df = pd.read_json (r'filename.json', lines=True)

df.to_csv (r' filename.csv', index = None)