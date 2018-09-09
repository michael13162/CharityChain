CREATE TABLE user (
  username TEXT NOT NULL,
  password TEXT NOT NULL,
  is_charity INTEGER NOT NULL,
  ein TEXT NOT NULL
);

CREATE TABLE charity (
  ein TEXT NOT NULL,
  tag_line TEXT NOT NULL,
  charity_name TEXT NOT NULL,
  rating INTEGER NOT NULL
);
