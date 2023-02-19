import os
from app import db
from flask import session, abort, request
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import text

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin)")
        if "_ADMIN" in username:
            db.session.execute(
                sql, {"username": username, "password": hash_value, "admin": True})
        else:
            db.session.execute(
                sql, {"username": username, "password": hash_value, "admin": False})
        db.session.commit()
        return login(username, password)
    except:
        return False

def login(username, password):
    sql = text("SELECT id, password, username FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user[1], password):
            session["user_id"] = user[0]
            session["user_name"] = user[2]
            session["csrf_token"] = os.urandom(16).hex()
            session["admin_privilege"] = user[3]
            return True

def user_id():
    return session.get("user_id", 0)

def user_admin():
    if session.get("admin_privilege", 0) == True:
        return True
    else:
        return False


def logout():
    del session["user_id"]
    del session["user_name"]


def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)


def delete_all():
    sql = text("TRUNCATE TABLE users CASCADE")
    db.session.execute(sql)
    db.session.commit()


def find_all():
    sql = text("SELECT * FROM users")
    result = db.session.execute(sql).fetchall()
    print(result)
    return result