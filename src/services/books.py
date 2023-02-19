from app import db
from datetime import datetime
from flask import session, abort, request
from sqlalchemy import text

def find_all_books():
    sql = text("SELECT * FROM books")
    books = db.session.execute(sql).fetchall()
    return books

def add_books(name: str, amount: int):
    try:
        sql = text("INSERT INTO books (name, amount) VALUES (:name, :amount)")
        db.session.execute(sql, {"name": name, "amount": amount})
        db.session.commit()
    except:
        return False

def borrow_books():
    #actual function of borrowing
    pass

def delete_all():
    sql = text("TRUNCATE TABLE books CASCADE")
    db.session.execute(sql)
    db.session.commit()