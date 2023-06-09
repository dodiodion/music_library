DROP TABLE IF EXISTS user_accounts CASCADE;
DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS user_accounts_id_seq;

CREATE SEQUENCE IF NOT EXISTS user_accounts_id_seq;
CREATE TABLE user_accounts (
  id SERIAL PRIMARY KEY,
  email_address text,
  username text
);

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  number_of_views int,
  user_account_id int,
  constraint fk_user_account foreign key(user_account_id)
    references user_accounts(id)
    on delete cascade
);

INSERT INTO user_accounts (email_address, username) VALUES ('bob@gmail.com', 'bob1');
INSERT INTO user_accounts (email_address, username) VALUES ('coxinha@hotmail.com', 'coxinha1995');
INSERT INTO user_accounts (email_address, username) VALUES ('poutine@mail.com', 'poutine44');
INSERT INTO user_accounts (email_address, username) VALUES ('feijoada@intel.it', 'feijoada983');