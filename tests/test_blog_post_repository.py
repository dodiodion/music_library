from lib.blog_post import *
from lib.blog_post_repository import *
from lib.comment import *
"""
Find a blog_post using its id, 
and return the blog_post with all its comments
"""
def test_find_with_comments(db_connection):
    db_connection.seed("seeds/blog.sql")
    repository = BlogPostRepository(db_connection)
    blog_post = repository.find_with_comments(1)
    assert blog_post == BlogPost(1, "Learn Databases", "SQL, TablePlus", [
        Comment(1, "Cool", "Bob", 1), 
        Comment(2, "Very helpful", "Vlad", 1)
        ])