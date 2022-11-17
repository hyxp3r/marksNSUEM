import pandas as pd
import os
from datetime import datetime
from connection import ConnectionPSQL, ConnectionSQL
from getData import GetDataSql, GetQueryFile
from addMeta import MakeDf
from insert import InsertTable
from telegram import SendMessage
from dotenv import load_dotenv
load_dotenv(".env")

createdTime = datetime.today()
createdTime = createdTime.strftime("%d-%m-%Y %H:%M:%S") 
sendMess = SendMessage(os.environ.get("bot_token"), os.environ.get("bot_chatID"))

cxnx = ConnectionSQL(os.environ.get("serverSQL"),os.environ.get("dbnameSQL") 
,os.environ.get("userSQL") , os.environ.get("passSQL")).connect()


query_marks = GetQueryFile("queryMarks.sql").read()
df_marks = GetDataSql(cxnx, query_marks).getData()

query_students = GetQueryFile("queryStudents.sql").read()
df_students = GetDataSql(cxnx, query_students ).getData()
df_students["Дата записи"] = createdTime

df_stat = MakeDf(df_students).make()

conn = ConnectionPSQL(os.environ.get("dbnamePSQL"), os.environ.get("userPSQL")
,os.environ.get("passwordPSQL"), os.environ.get("hostPSQL"))

append_marks = InsertTable(os.environ.get("userPSQL")
,os.environ.get("passwordPSQL"), os.environ.get("hostPSQL"),os.environ.get("dbnamePSQL") ).replace(df_marks, "marks")

send_message_marks = sendMess.sendMessageMarks()

append_students = InsertTable(os.environ.get("userPSQL")
,os.environ.get("passwordPSQL"), os.environ.get("hostPSQL"),os.environ.get("dbnamePSQL") ).append(df_students, "students")

send_message_students = sendMess.sendMessageStudents()

append_stat = InsertTable(os.environ.get("userPSQL")
,os.environ.get("passwordPSQL"), os.environ.get("hostPSQL"),os.environ.get("dbnamePSQL") ).append(df_stat, "stat")

send_message_stat = sendMess.sendMessageStat(df_students)






