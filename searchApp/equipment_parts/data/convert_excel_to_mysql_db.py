from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
DB_NAME = "main"

print(Path(__file__).resolve().parent.parent)

df = pd.read_excel(f"{Path(__file__).resolve().parent.parent}/data/excel_data.xlsx")

engine = create_engine(f'mysql+mysqlconnector://root:root@localhost:3306/{DB_NAME}', echo=False)
con = engine.connect()

r = con.execute("show tables")
if r.rowcount >= 1:
    print(f"The database {DB_NAME} is not empty, contains the following tables: {r.fetchall()}")
    exit(0)

con.execute("create table details ("
            "id int not null primary key AUTO_INCREMENT, "
            "asv_id int  null, "
            "full_name text not null)")

n = 100000  # chunk row size
list_df = [df[i:i+n] for i in range(0, df.shape[0], n)]
for index, df_item in enumerate(list_df):
    df_item.to_sql(name='details', con=con, if_exists='append', index=False, )
    print(f"chunk.index.{index}")

con.close()

