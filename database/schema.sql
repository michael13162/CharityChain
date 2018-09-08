CREATE TABLE users (
  uid integer PRIMARY KEY,
  email text NOT NULL,
  password text NOT NULL
);

CREATE TABLE charities (
  cid integer PRIMARY KEY,
  ein text NOT NULL
);
