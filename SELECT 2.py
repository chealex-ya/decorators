import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://ruachaj:Tachamasib1@localhost:5432/chealex_db')
engine

connection = engine.connect()

sel = connection.execute("""
SELECT genre_id, 
COUNT(singer_id) 
FROM SingerGenre 
GROUP BY genre_id;""").fetchall()
print(f'\n1. Количество исполнителей в каждом жанре: {sel}')

sel = connection.execute("""
SELECT COUNT(t.id) count
FROM trek t
JOIN album a ON t.album_id = a.id
WHERE a.year BETWEEN 2019 AND 2020
;""").fetchall()
print(f'\n2. {sel[0][0]} - треков, вошедших в альбомы 2019-2020 годов')

sel = connection.execute("""
SELECT a.title, AVG(t.duration) average
FROM trek t
JOIN album a ON t.album_id = a.id
GROUP BY a.title
;""").fetchall()
print(f'\n3. Средняя продолжительность треков по каждому альбому: {sel}')

# все исполнители, которые не выпустили альбомы в 2020 году
sel = connection.execute("""
SELECT DISTINCT s.name
FROM singer s
JOIN albumsinger a_s ON s.id = a_s.singer_id
JOIN album a ON a_s.album_id = a.id
GROUP BY a.year, s.name
HAVING a.year != 2020
;""").fetchall()
print(f'\n4. Исполнители, не выпустившие альбомы в 2020 году: {sel}')

sel = connection.execute("""
SELECT mix_tape.name
FROM mixtape mix_tape
JOIN mixtrek mxt ON mix_tape.ID = mxt.mixtape_ID
JOIN trek t ON mxt.trek_ID = t.ID
JOIN album a ON t.album_ID = a.ID
JOIN albumsinger a_s ON a.id = a_s.album_id
JOIN singer s ON a_s.singer_id = s.id
WHERE s.name = 'Cool singer'
;""").fetchall()
print(f'\n5. Все сборники, где есть треки исполнителя Cool Singer: {sel}')

# название альбомов, в которых присутствуют исполнители более 1 жанра;
sel = connection.execute("""
SELECT DISTINCT a.title
FROM album a
JOIN albumsinger a_s ON a.ID = a_s.album_ID
JOIN singer s ON a_s.singer_ID = s.ID
WHERE s.name = (
    SELECT s.name
    FROM singer s
    JOIN singergenre s_g ON s.ID = s_g.singer_ID
    JOIN genre g ON s_g.genre_ID = g.ID
    GROUP BY s.name
    HAVING COUNT(s.name) > 1)
""").fetchall()
print(f'\n6. Названия альбомов, в которых присутствуют исполнители более 1 жанра: {sel}')

# наименования треков, которые не входят в сборники
sel = connection.execute("""
SELECT t.title
FROM mixtape mix_tape
FULL OUTER JOIN mixtrek mxt ON mix_tape.ID = mxt.mixtape_ID
FULL OUTER JOIN trek t ON mxt.trek_ID = t.ID
GROUP BY mix_tape.id, mxt.mixtape_id, mxt.trek_id, t.id
HAVING mix_tape.id IS NULL
""").fetchall()
print(f'\n7. Названия треков, которые не входят в сборники: {sel}')

sel = connection.execute("""
SELECT DISTINCT s.name
FROM trek t
JOIN album a ON t.album_id = a.id
JOIN albumsinger a_s ON a.ID = a_s.album_ID
JOIN singer s ON a_s.singer_ID = s.ID
WHERE t.duration = (
    SELECT MIN(t.duration) min_duration
    FROM trek t)
;""").fetchall()
print(f'\n8. Имена исполнителей, написавших самый короткий по продолжительности трек: {sel}')

sel = connection.execute(f"""
SELECT a.title
    FROM trek t
    JOIN album a ON t.album_id = a.id
    GROUP BY a.title
    HAVING COUNT(t.title) = (
        SELECT  COUNT(t.title) trek_counter
        FROM trek t
        JOIN album a ON t.album_id = a.id
        GROUP BY a.title
        ORDER BY trek_counter
        LIMIT 1)
;""").fetchall()
print(f'\n9. Альбомы с наименьшим количеством треков: {sel}')