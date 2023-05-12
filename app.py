# file: app.py
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection
from lib.cohort_repository import CohortRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!

        # artist_repository = ArtistRepository(self._connection)
        # artists = artist_repository.all()
        # album_repository = AlbumRepository(self._connection)
        # albums = album_repository.all()
        # print("Welcome to the music library manager!")
        # print("What would you like to do? \n 1 - List all albums \n 2 - List all artists\n")
        # choice = input("Enter your choice: ")
        # if(choice == "1"):
        #     for album in albums:
        #         print(f"{album.id} - {album.title})")
        # elif(choice == "2"):
        #     for artist in artists:
        #         print(f"{artist.id}: {artist.name} ({artist.genre})")
        # else: print (f"This is not a choice: {choice}")
        cohort_repository = CohortRepository(self._connection)
        print(cohort_repository.find_with_students(1))

if __name__ == '__main__':
    app = Application()
    app.run()