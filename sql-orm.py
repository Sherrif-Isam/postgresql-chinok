from sqlalchemy import create_engine, Column, Float, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the database engine
db = create_engine("postgresql:///chinook")
base = declarative_base()

# Define your classes representing the tables
class Artist(base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)

class Album(base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("artist.artist_id"))

class Track(base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("album.album_id"))
    media_type_id = Column(Integer, primary_key=False)
    genre_id = Column(Integer, primary_key=False)
    composer = Column(String)
    milliseconds = Column(Integer)
    bytes = Column(Integer)
    unit_price = Column(Float)

# Create a session
Session = sessionmaker(db)
session = Session()

# Create the tables in the database
base.metadata.create_all(db)

# Query and print artists
#artists = session.query(Artist).all()
#for artist in artists:
    #print(artist.artist_id, artist.name, sep=" | ")

# Query 1 - select all records from the "Artist" table
#artists = session.query(Artist)
#for artist in artists:
      #print(artist.ArtistId, artist.Name, sep=" | ")



# Query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - select only "Queen" from the "Artist" table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
tracks = session.query(Track).filter_by(composer="Queen")
for track in tracks:
    print(
        track.track_id,
        track.name,
        track.album_id,
        track.media_type_id,
        track.genre_id,
        track.composer,
        track.milliseconds,
        track.bytes,
        track.unit_price,
        sep=" | "
    )