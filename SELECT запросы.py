import sqlalchemy
from pprint import pprint
import pandas as pd
import random

engine = sqlalchemy.create_engine('postgresql://ruachaj:Tachamasib1@localhost:5432/chealex_db')
engine

connection = engine.connect()
# название и год выхода альбомов, вышедших в 2018 году
sel = connection.execute("""SELECT title,year FROM album WHERE year > 2018;""").fetchall()
print(pd.DataFrame(sel))

# название и продолжительность самого длительного трека
max = (connection.execute("""SELECT MAX(duration) FROM trek;""").fetchall())[0][0]
sel = connection.execute(f"""SELECT Title FROM trek WHERE duration = {max};""").fetchall()
print(pd.DataFrame(sel))

# название треков, продолжительность которых не менее 3,5 минуты
sel = connection.execute(f"""SELECT Title FROM trek WHERE duration >3.5;""").fetchall()
print(pd.DataFrame(sel))

# названия сборников, вышедших в период с 2018 по 2020 год включительно
sel = connection.execute(f"""SELECT name FROM mixtape WHERE year BETWEEN 2018 AND 2022;""").fetchall()
print(pd.DataFrame(sel))

# исполнители, чье имя состоит из 1 слова
name = connection.execute(f"""SELECT name FROM singer;""").fetchall()
for i in name:
    if (len(i[0].split(" ")))>1:
        print(i)

# название треков, которые содержат слово "мой"/"my"
sel1 = connection.execute(f"""SELECT Title FROM trek WHERE Title iLIKE '%%my%%';""").fetchall()
sel2 = connection.execute(f"""SELECT Title FROM trek WHERE Title iLIKE '%%мой%%';""").fetchall()
print(*sel1, *sel2)