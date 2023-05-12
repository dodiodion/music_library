from lib.comment import *
from lib.blog_post import *

class BlogPostRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_with_comments(self, blog_post_id):
        rows = self._connection.execute(
            "SELECT blog_posts.id AS blog_post_id, blog_posts.title AS blog_post_title, blog_posts.content AS blog_post_content, comments.id AS comment_id, comments.comment_content AS comment_content, comments.author AS author " \
            "FROM blog_posts JOIN comments ON blog_post_id = comments.blog_post_id " \
            "WHERE blog_post_id =%s", [blog_post_id])
        comments = []
        for row in rows:
            comment = Comment(row["comment_id"], row["comment_content"], row["author"], row["blog_post_id"])
            comments.append(comment)
        blog_post = BlogPost(rows[0]["blog_post_id"], rows[0]["blog_post_title"], rows[0]["blog_post_content"], comments)
        return blog_post