from db import db
from app import app

application = app
application.app_context().push()


def create_tables():
    db.session.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        );
    """)

    db.session.commit()


def drop_tables():
    db.session.execute("""
        DROP TABLE IF EXISTS users CASCADE;
    """)

    db.session.commit()


def initialize_database():
    drop_tables()
    create_tables()


if __name__ == "__main__":
    initialize_database()