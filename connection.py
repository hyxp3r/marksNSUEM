import psycopg2 as ps
import pyodbc
import dotenv
import os




class ConnectionSQL:

    def __init__(self, server:str, database:str, username:str, password:str) -> None:

        self.server = server
        self.database = database
        self.username = username
        self.password = password


    def connect(self) -> object:

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        
        return cnxn



class ConnectionPSQL:

    def __init__(self, dbname:str, user:str, password:str, host:str) -> None:
        
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host

    def connect(self):

        conn = ps.connect(
                        dbname = self.dbname,
                        user = self.user,
                        password = self.password,
                        host = self.host
                        )

        cursor = conn.cursor()

        return cursor