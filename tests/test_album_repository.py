from lib.album_repository import AlbumRepository
from lib.album import Album
"""
When we call AlbumRepository.all()
we get a list of the Album objects coming from the seed data
"""
def test_get_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    albums = repository.all()
    assert albums == [
            Album (1, 'Doolittle', 1989, 1),
            Album (2, 'Surfer Rosa', 1988, 1),
            Album (3, 'Waterloo', 1974, 2),
            Album (4, 'Super Trouper', 1980, 2),
            Album (5, 'Bossanova', 1990, 1),
            Album (6, 'Lover', 2019, 3),
            Album (7, 'Folklore', 2020, 3),
            Album (8, 'I Put a Spell on You', 1965, 4),
            Album (9, 'Baltimore', 1978, 4),
            Album (10, 'Here Comes the Sun', 1971, 4),
            Album (11, 'Fodder on My Wings', 1982, 4),
            Album (12, 'Ring Ring', 1973, 2)]
    
def test_find_single_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    album = repository.find(2)
    assert album == Album(2, 'Surfer Rosa', 1988, 1)


"""
Given a new album, AlbumRepository#create a new album object to the database
"""

def test_create_new_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.create(Album(None, "Test Album Name", 1990, 2))
    result = repository.all()
    assert result == [
        Album (1, 'Doolittle', 1989, 1),
        Album (2, 'Surfer Rosa', 1988, 1),
        Album (3, 'Waterloo', 1974, 2),
        Album (4, 'Super Trouper', 1980, 2),
        Album (5, 'Bossanova', 1990, 1),
        Album (6, 'Lover', 2019, 3),
        Album (7, 'Folklore', 2020, 3),
        Album (8, 'I Put a Spell on You', 1965, 4),
        Album (9, 'Baltimore', 1978, 4),
        Album (10, 'Here Comes the Sun', 1971, 4),
        Album (11, 'Fodder on My Wings', 1982, 4),
        Album (12, 'Ring Ring', 1973, 2),
        Album (13, "Test Album Name", 1990, 2)]
    

"""
Given an album to delete, AlbumRepository#delete the album object from the database
"""
    
def test_create_new_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(10)
    result = repository.all()
    assert result == [
        Album (1, 'Doolittle', 1989, 1),
        Album (2, 'Surfer Rosa', 1988, 1),
        Album (3, 'Waterloo', 1974, 2),
        Album (4, 'Super Trouper', 1980, 2),
        Album (5, 'Bossanova', 1990, 1),
        Album (6, 'Lover', 2019, 3),
        Album (7, 'Folklore', 2020, 3),
        Album (8, 'I Put a Spell on You', 1965, 4),
        Album (9, 'Baltimore', 1978, 4),
        Album (11, 'Fodder on My Wings', 1982, 4),
        Album (12, 'Ring Ring', 1973, 2)]