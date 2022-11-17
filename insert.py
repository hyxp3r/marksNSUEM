from sqlalchemy import create_engine
import pandas as pd

class InsertTable:

    def __init__(self, username:str, password:str, host:str, base:str) -> None:

        self.engine = create_engine(f'postgresql://{username}:{password}@{host}/{base}')

    def replace(self, df, table):

        with self.engine.connect() as con:
            con.execute(f'DELETE FROM {table}')
    
        df.to_sql(f"{table}", self.engine, if_exists = 'append', index=False)

    def append(self, df, table):
    
        df.to_sql(f"{table}", self.engine, if_exists = 'append', index=False)




    