from lib.post import *
"""
given a post, verify that it contructs with an id, a title, content, user_account_id and number_of_views
"""

def test_post_constructs():
    post = Post(1, "Test Title", "Test Content", 1, 10)
    assert post.id == 1
    assert post.title == "Test Title"
    assert post.content == "Test Content"
    assert post.user_account_id == 1
    assert post.number_of_views == 10