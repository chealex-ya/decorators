import sqlalchemy
import pandas as pd
import random

with engine.connect() as connection:
    connection.execute("""DELETE FROM mixtrek WHERE MixTape_ID > 0;""")
    connection.execute("""DELETE FROM trek WHERE ID > 0;""")
    connection.execute("""DELETE FROM AlbumSinger WHERE album_id > 0;""")
    connection.execute("""DELETE FROM SingerGenre WHERE singer_id > 0;""")
    connection.execute("""DELETE FROM singer WHERE ID > 0;""")
    connection.execute("""DELETE FROM album WHERE ID > 0;""")
    connection.execute("""DELETE FROM genre WHERE ID > 0;""")
    connection.execute("""DELETE FROM mixtape WHERE ID > 0;""")


# SINGER
with engine.connect() as connection:
    x = 1
    name = "'Singer'"
    while x < 8:
        result = connection.execute(f"""INSERT INTO singer (ID, Name) values ({x},{name}'{x}')""")
        x = x+1
    result = connection.execute(f"""INSERT INTO singer (ID, Name) values (8,'Имя Фамилия')""")
    sel = connection.execute("""SELECT * FROM singer;""").fetchall()
    print(f'{name}')
    print(pd.DataFrame(sel))

# ALBUM
with engine.connect() as connection:
    x = 1
    name = "'Album'"
    while x < 9:
        year = random.randint(2017,2020)
        result = connection.execute(f"""INSERT INTO Album (id, title, year) values ({x},{name}'{x}',{year})""")
        x = x+1
    sel = connection.execute("""SELECT * FROM Album;""").fetchall()
    print(f'\n{name}')
    print(pd.DataFrame(sel))


# AlbumSinger
with engine.connect() as connection:
    album_id = connection.execute("""SELECT id FROM Album;""").fetchall()
    for a in album_id:
        b = random.randint(1,8)
        result = connection.execute(f"""INSERT INTO AlbumSinger (album_id, singer_id) values ({a[0]},{b})""")
    sel = connection.execute("""SELECT * FROM AlbumSinger;""").fetchall()
    print(pd.DataFrame(sel))

#GENRE
with engine.connect() as connection:
    x = 1
    name = "'Genre'"
    while x < 6:
        result = connection.execute(f"""INSERT INTO genre (id, Name) values ({x}, {name}'{x}')""")
        x =x+1
    sel = connection.execute("""SELECT * FROM genre;""").fetchall()
    print(pd.DataFrame(sel))
    print("\n")

# SingerGenre
print("SingerGenre")
with engine.connect() as connection:
    singer_id = connection.execute("""SELECT id FROM singer;""").fetchall()
    for a in singer_id:
        b = random.randint(1, 5)
        result = connection.execute(f"""INSERT INTO SingerGenre (genre_id, singer_id) values ({b},{a[0]})""")
    sel = connection.execute("""SELECT * FROM SingerGenre;""").fetchall()
    print(pd.DataFrame(sel))

# Trek
print("Trek")
with engine.connect() as connection:
    x = 1
    title = "'Trek'"
    while x < 15:
        duration = random.randint(3, 5)
        album_id = random.randint(1, 8)
        result = connection.execute(f"""INSERT INTO trek (id, album_id, duration, title) values ({x},{album_id},{duration},{title}'{x}')""")
        x =x+1
    result = connection.execute(
        f"""INSERT INTO trek (id, album_id, duration, title) values (15,1,4,'My trek')""")
    sel = connection.execute("""SELECT * FROM trek;""").fetchall()
    print(pd.DataFrame(sel))

print("\n")

# MixTape
print("MixTape")
with engine.connect() as connection:
    x = 1
    name = "'MixTape'"
    while x < 9:
        year = random.randint(2016, 2020)
        result = connection.execute(f"""INSERT INTO mixtape (id, name, year) values ({x}, {name}'{x}', {year})""")
        x =x+1
    sel = connection.execute("""SELECT * FROM mixtape;""").fetchall()
    print(pd.DataFrame(sel))

# # MixTrek
print("MixTrek")
with engine.connect() as connection:
    trek_id = connection.execute("""SELECT id FROM trek;""").fetchall()
    for a in trek_id:
        b = random.randint(1, 8)
        result = connection.execute(f"""INSERT INTO MixTrek (mixtape_ID, trek_id) values ({b},{a[0]})""")
    sel = connection.execute("""SELECT * FROM MixTrek;""").fetchall()
    print(pd.DataFrame(sel))

sel = connection.execute("""
INSERT INTO mixtape (ID, Name, Year) values (100, 'Cool Mix', 1950);
INSERT INTO album (ID, title, year) values (10, 'Cool album', 1940);
INSERT INTO singer (ID, name) values (15, 'Cool singer');
INSERT INTO trek (ID, Album_ID, Duration, Title) values (120, 10, 4, 'Cool song');
INSERT INTO mixtrek (mixtape_ID, trek_ID) values (100, 120);
INSERT INTO albumsinger (album_ID,singer_ID) values (10, 15);
""")

upd = connection.execute("""
INSERT INTO SingerGenre (Genre_ID, Singer_ID) values (1, 15);
INSERT INTO SingerGenre (Genre_ID, Singer_ID) values (2, 15);
""")

upd = connection.execute("""
DELETE FROM mixtape
WHERE ID = 5;
""")

upd = connection.execute("""
DELETE FROM mixtape
WHERE ID = 6;
""")