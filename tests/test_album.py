from lib.album import Album

"""
Album contructs with an title, release_year and artist id.
"""
def test_album_constructs():
    album = Album("Test album", 2013, 4)
    assert album.title == "Test album"
    assert album.release_year == 2013
    assert album.artist_id == 4

"""
We can compare two identical albums
and have them be equal
"""
def test_albums_equal():
    album1 = Album(1, "Test Album", 2045)
    album2 = Album(1, "Test Album", 2045)
    assert album1 == album2