from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.recipe_repository import RecipeRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
for artist in artists:
    print(artist)

#Retrieve all albums
album_repository = AlbumRepository(connection)

# List them out
for album in album_repository.all():
    print(album)

print(album_repository.find(2))

recipe_repository = RecipeRepository(connection)
for recipe in recipe_repository.all():
    print(recipe)

print(recipe_repository.find(4))