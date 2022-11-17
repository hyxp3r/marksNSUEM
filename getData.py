import pandas as pd


class GetDataSql:

    def __init__(self,cxnx:object, query:object) -> None:
        
        self.cxnx = cxnx
        self.query = query

    def getData(self):

        data = pd.read_sql_query(self.query, self.cxnx)
        df = pd.DataFrame(data)

        return df



class GetQueryFile:

    def __init__(self, path:str) -> None:

        self.path = path

    def read(self):
        
        file = open(self.path, 'r')
        query = file.read()
        file.close()

        return query