CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    amount INTEGER
);

CREATE TABLE borrowed (
        id SERIAL PRIMARY KEY,
        user_id SERIAL,
        book_id SERIAL,
        borrow_date DATE,
        return_date DATE 
);