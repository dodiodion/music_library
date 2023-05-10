DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    recipe_name text,
    cooking_time int,
    rating int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('pizza', 45, 4);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('coxinha', 60, 4);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('poutine', 15, 3);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('feijoada', 120, 5);