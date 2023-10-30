-- name, age, breed, image_url, owner_id
CREATE TABLE IF NOT EXISTS dogs (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    breed TEXT,
    image_url TEXT,
    owner_id INTEGER,
    FOREIGN KEY (owner_id) REFERENCES owners(id)
);

CREATE TABLE IF NOT EXISTS owners (
    id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    email TEXT,
    phone TEXT
);
-- add column to existing table
ALTER TABLE dogs ADD favorite_treats TEXT;

DROP TABLE dogs;
DROP TABLE owners;