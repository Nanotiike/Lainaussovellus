from db import db
from app import app

application = app
application.app_context().push()


def create_tables():
    db.session.execute("""
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
    """)

    db.session.commit()


def drop_tables():
    db.session.execute("""
        DROP TABLE IF EXISTS users CASCADE;
        DROP TABLE IF EXISTS books CASCADE;
        DROP TABRE IF EXISTS borrowed CASCADE;
    """)

    db.session.commit()


def initialize_database():
    drop_tables()
    create_tables()


if __name__ == "__main__":
    initialize_database()