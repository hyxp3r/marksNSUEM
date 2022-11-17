import requests
import pandas as pd
from datetime import datetime

class SendMessage:

    message_marks = """Таблица <b>"Оценки"</b> успешно записана в PostgreSQL"""
    message_students = """Таблица <b>"Студенты"</b> успешно записана в PostgreSQL"""

    def __init__(self, bot_token:str, bot_chatID:str) -> None:

        self.bot_token = bot_token
        self.bot_chatID = bot_chatID
        self.send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text=' 

    def sendMessageStudents(self):

        send_text = self.send_text + self.message_students
        self.send(send_text)

    def sendMessageMarks(self):

        send_text = self.send_text + self.message_marks
        self.send(send_text)

    def sendMessageStat(self, df:object):

        createdTime = datetime.today()
        createdTime = createdTime.strftime("%d-%m-%Y %H:%M:%S") 

        text = f"""
Таблица <b>"Статистика"</b> успешно записана в PostgreSQL

Количество студентов: <b>{df.shape[0]}</b>
Количество оценок: <b>{df["Всего оценок"].sum()}</b>
Кол-во отл. оценок: <b>{df["Кол-во отл. оценок"].sum()}</b>
Кол-во хор. оценок: <b>{df["Кол-во хор. оценок"].sum()}</b>
Кол-во удовл. оценок: <b>{df["Кол-во удовл. оценок"].sum()}</b>
Кол-во зачтено: <b>{df["Кол-во зачтено"].sum()}</b>
Кол-во неудовл. оценок: <b>{df["Кол-во неудовл. оценок"].sum()}</b>
Кол-во не допущен: <b>{df["Кол-во не допущен"].sum()}</b>
Кол-во не зачтено: <b>{df["Кол-во не зачтено"].sum()}</b>
Кол-во неявок (неуваж): <b>{df["Кол-во неявок (неуваж)"].sum()}</b>
Кол-во неявок (уваж): <b>{df["Кол-во неявок (уваж)"].sum()}</b>
Кол-во не должен сдавать: <b>{df["Кол-во не должен сдавать"].sum()}</b>
"""

        send_text = self.send_text + text

        self.send(send_text)



    def send(self, send_text:str):

        response = requests.get(send_text)


    