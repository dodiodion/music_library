Two Tables Design Recipe Template

Copy this recipe template to design and create two related database tables from a specification.

1. Extract nouns from the user stories or specification

# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.

Nouns:

students, student name, cohort name, starting dates, cohorts

2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

Record | Properties
student | student name
cohort | cohort name, starting date

Name of the first table (always plural): students

Column names: student_name

Name of the second table (always plural): cohorts

Column names: cohort_name, starting_date

3. Decide the column types

Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

Table: students
id: SERIAL
student_name: text

Table: cohort
id: SERIAL
cohort_name: text
starting_date: text

4. Decide on The Tables Relationship

Most of the time, you'll be using a one-to-many relationship, and will need a foreign key on one of the two tables.

To decide on which one, answer these two questions:

Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)
You'll then be able to say that:

[A] has many [B]
And on the other side, [B] belongs to [A]
In that case, the foreign key is in the table [B]
Replace the relevant bits in this example with your own:

# EXAMPLE

1. Can one cohort have many students? YES
2. Can one student have many cohort? NO

-> Therefore,
-> A cohort HAS MANY students
-> A student BELONGS TO a cohort

-> Therefore, the foreign key is on the students table.

If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).

4. Write the SQL

-- EXAMPLE
-- file: students_directory_2.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.

CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  cohort_name text,
  starting_date text,
);

-- Then the table with the foreign key second.

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  student_name text,
  
-- The foreign key name is always {other_table_singular}_id
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
    on delete cascade
);
5. Create the tables

psql -h 127.0.0.1 database_name < albums_table.sql

------------------------
# Challenge Chapter 6:


1. Extract nouns from the user stories or specification

# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having a content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.

Nouns:

blog posts , title, content, comments, comments content, comment author

2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

Record | Properties
blog_posts | title, content
comments | content, author

Name of the first table (always plural): blog_posts

Column names: title, content

Name of the second table (always plural): comments

Column names: comment_content, author

3. Decide the column types

Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

Table: blog_posts
id: SERIAL
title: text
content: text

Table: comments
id: SERIAL
comment_content: text
author: text

4. Decide on The Tables Relationship

Most of the time, you'll be using a one-to-many relationship, and will need a foreign key on one of the two tables.

To decide on which one, answer these two questions:

Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)
You'll then be able to say that:

[A] has many [B]
And on the other side, [B] belongs to [A]
In that case, the foreign key is in the table [B]
Replace the relevant bits in this example with your own:

# EXAMPLE

1. Can one blog post have many comments? YES
2. Can one comment have many blog posts? NO

-> Therefore,
-> A blog post HAS MANY comments
-> A comment BELONGS TO a blog post

-> Therefore, the foreign key is on the comments table.

If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).

4. Write the SQL

-- EXAMPLE
-- file: blog.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.

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
5. Create the tables

psql -h 127.0.0.1 music_library < seeds/blog.sql