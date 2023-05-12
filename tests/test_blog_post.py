from lib.blog_post import *
"""
Given a post,
we want to construct blog post object with id, title and content
"""
def test_blog_post_init():
    blog_post = BlogPost(1, "Test Title", "Test Content")
    assert blog_post.id == 1
    assert blog_post.title == "Test Title"
    assert blog_post.content == "Test Content"

"""
We can format blog posts to strings nicely
"""
def test_blog_post_format_nicely():
    blog_post = BlogPost(1, "Test Title", "Test Content")
    assert str(blog_post) == "BlogPost(1, Test Title, Test Content, [])"

"""
We can compare two identical blog posts
And have them be equal
"""
def test_blog_posts_are_equal():
    blog_post1 = BlogPost(1, "Test Title", "Test Content")
    blog_post2 = BlogPost(1, "Test Title", "Test Content")
    assert blog_post1 == blog_post2