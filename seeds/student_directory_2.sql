DROP TABLE IF EXISTS cohorts CASCADE;
DROP TABLE IF EXISTS students CASCADE;
DROP SEQUENCE IF EXISTS cohorts_id_seq;

CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  cohort_name text,
  starting_date text);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  student_name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
    on delete cascade
);

INSERT INTO cohorts (cohort_name, starting_date) VALUES ('Summer 2021', '12-06-2021');

INSERT INTO students (student_name, cohort_id) VALUES ('Bob Builder', 1);
INSERT INTO students (student_name, cohort_id) VALUES ('Vladimir Putin', 1)