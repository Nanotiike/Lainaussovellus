from app import db
from datetime import datetime
from dateutil.relativedelta import relativedelta
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
        return True
    except:
        return False

def borrow_books(user_id, book_id):
    try:
        return_date = datetime.today() + relativedelta(month=1)
        sql = text("INSERT INTO borrowed (user_id, book_id, borrow_date, return_date) VALUES (:user, :book, :borrow, :return)")
        db.session.execute(sql, {"user": user_id, "book": book_id, "borrow": datetime.today().strftime("%Y-%m-%d"), "return": return_date})
        return True
    except:
        return False

def delete_all():
    sql = text("TRUNCATE TABLE books CASCADE")
    db.session.execute(sql)
    db.session.commit()