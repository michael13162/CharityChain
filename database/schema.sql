CREATE TABLE user (
  username TEXT NOT NULL,
  password TEXT NOT NULL,
  account_id TEXT NOT NULL,
  is_charity INTEGER NOT NULL,
  ein TEXT NOT NULL
);

CREATE TABLE charity (
  ein TEXT NOT NULL,
  tag_line TEXT NOT NULL,
  charity_name TEXT NOT NULL,
  mission_statement TEXT NOT NULL,
  rating INTEGER NOT NULL
);

CREATE TABLE trans (
  username TEXT NOT NULL,
  ein TEXT NOT NULL,
  amount REAL NOT NULL,
  description TEXT NOT NULL
);
