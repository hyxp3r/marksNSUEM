import pandas as pd
from datetime import datetime


class MakeDf:

    def __init__(self, df:object) -> None:
        self.df = df
        
    

    def make(self):


        createdTime = datetime.today()
        createdTime = createdTime.strftime("%d-%m-%Y %H:%M:%S") 

        stat = {

        "Дата записи": createdTime,
        "Количество студентов":self.df.shape[0],
        "Количество оценок": self.df["Всего оценок"].sum(),
        "Кол-во отл. оценок":self.df["Кол-во отл. оценок"].sum(),
        "Кол-во хор. оценок": self.df["Кол-во хор. оценок"].sum(),
        "Кол-во удовл. оценок":self.df["Кол-во удовл. оценок"].sum(),
        "Кол-во зачтено": self.df["Кол-во зачтено"].sum(),
        "Кол-во неудовл. оценок":self.df["Кол-во неудовл. оценок"].sum(),
        "Кол-во не допущен": self.df["Кол-во не допущен"].sum(),
        "Кол-во не зачтено":self.df["Кол-во не зачтено"].sum(),
        "Кол-во неявок (неуваж)": self.df["Кол-во неявок (неуваж)"].sum(),
        "Кол-во неявок (уваж)": self.df["Кол-во неявок (уваж)"].sum(),
        "Кол-во не должен сдавать": self.df["Кол-во не должен сдавать"].sum(),

       }
        stat = pd.DataFrame(stat, index=[0])
     
        return stat

