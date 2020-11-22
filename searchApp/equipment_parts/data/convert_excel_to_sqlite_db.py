import sqlite3
from pathlib import Path

import pandas as pd

print(Path(__file__).resolve().parent.parent)

df = pd.read_excel(f"{Path(__file__).resolve().parent.parent}/Data/excel_data.xlsx")

db_conn = sqlite3.connect(f"{Path(__file__).resolve().parent.parent}/db.sqlite3")

c = db_conn.cursor()

# c.execute("CREATE TABLE details (asv_id INTEGER , full_name TEXT NOT NULL);")

df.to_sql('details', db_conn, if_exists='append', index=False)

