class Comment:
    def __init__(self, id, comment_content, author, blog_post_id):
        self.id = id
        self.comment_content = comment_content
        self.author = author
        self.blog_post_id = blog_post_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Comment({self.id}, {self.comment_content}, {self.author})"
        