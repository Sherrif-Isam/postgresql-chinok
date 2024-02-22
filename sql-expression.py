from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

db = create_engine("postgresql:///chinook")
meta = MetaData(bind=db)  # Use bind parameter to pass the engine instance

artist_table = Table(
    "artist", meta, 
    Column("artist_id", Integer, primary_key=True),
    Column("name", String)
)

album_table = Table(
    "album", meta, 
    Column("album_id", Integer, primary_key=True),
    Column("title", String),
    Column("artist_id", Integer, ForeignKey("artist.artist_id"))  # Corrected ForeignKey declaration
)

track_table = Table(
    "track", meta, 
    Column("track_id", Integer, primary_key=True),
    Column("name", String),
    Column("album_id", Integer, ForeignKey("album.album_id")),  # Corrected ForeignKey declaration
    Column("media_type_id", Integer, primary_key=False),
    Column("genre_id", Integer, primary_key=False),
    Column("composer", String),
    Column("milliseconds", Integer),
    Column("bytes", Integer),
    Column("unit_price", Float)
)

with db.connect() as connection: 
    select_query = artist_table.select()
    results = connection.execute(select_query)
    for result in results:
        print(result)
