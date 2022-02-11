import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://ruachaj:Tachamasib1@localhost:5432/chealex_db')
engine

connection = engine.connect()

connection.execute("""
CREATE TABLE Singer
(ID serial primary key,
Name varchar(50) not null);

create table if not exists Album (
ID serial primary key,
Singer_ID integer not null references Singer(ID),
Title varchar(30) not null,
Year integer not null, check(Year>1900 and Year<2021)
);

create table if not exists Trek (
ID serial primary key,
Album_ID integer not null references Album(ID),
Duration integer not null,
Title varchar(30) not null
);

create table if not exists MixTape (
ID serial primary key,
Name varchar(50) not null,
Year integer not null, check(Year>1900 and Year<2021)
);

create table if not exists Genre (
ID serial primary key,
Name varchar(50) not null
);

create table if not exists AlbumSinger (
Album_ID integer references Album(ID),
Singer_ID integer references Singer(ID),
constraint album_singer primary key (Album_ID, Singer_ID)
);

create table if not exists MixTrek (
MixTape_ID integer references MixTape(ID),
Trek_ID integer references Trek(ID),
constraint mix_trek primary key (MixTape_ID, Trek_ID)
);

create table if not exists SingerGenre (
Genre_ID integer references Genre(ID),
Singer_ID integer references Singer(ID),
constraint genre_singer primary key (Genre_ID, Singer_ID)
);

""")