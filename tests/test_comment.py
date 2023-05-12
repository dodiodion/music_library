from lib.comment import *
"""
Given a comment,
we want to construct a comment object with id, comment content, author blog_post_id
"""
def test_comment_init():
    comment = Comment(1, "Test Content", "Test Author", 1)
    assert comment.id == 1
    assert comment.comment_content == "Test Content"
    assert comment.author == "Test Author"
    assert comment.blog_post_id == 1

    """
We can format students to strings nicely
"""
def test_comment_format_nicely():
    comment = Comment(1, "Test Comment", "Test Author", 1)
    assert str(comment) == "Comment(1, Test Comment, Test Author)"

"""
We can compare two identical students
And have them be equal
"""
def test_students_are_equal():
    comment1 = Comment(1, "Test Comment", "Test Author", 1)
    comment2 = Comment(1, "Test Comment", "Test Author", 1)
    assert comment1 == comment2