DROP TABLE IF EXISTS blog_posts CASCADE;
DROP TABLE IF EXISTS comments CASCADE;
DROP SEQUENCE IF EXISTS blog_posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS blog_posts_id_seq;
CREATE TABLE blog_posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text
);

-- Then the table with the foreign key second.

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    comment_content text,
    author text,

-- The foreign key name is always {other_table_singular}_id
    blog_post_id int,
    constraint fk_blog_post foreign key(blog_post_id)
    references blog_posts(id)
    on delete cascade
);

INSERT INTO blog_posts (title, content) VALUES ('Learn Databases', 'SQL, TablePlus');

INSERT INTO comments (comment_content, author, blog_post_id) VALUES ('Cool', 'Bob', 1);
INSERT INTO comments (comment_content, author, blog_post_id) VALUES ('Very helpful', 'Vlad', 1);
