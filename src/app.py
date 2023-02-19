from flask import Flask, render_template, request, redirect
import string
from db import db
from config import DATABASE_URL, SECRET_KEY
import services.users as users
import services.books as books
from sqlalchemy import text


app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
db.init_app(app)

@app.route("/")
def index():
    results = users.find_all()
    return render_template("index.html", users = results)

@app.route("/login", methods = ["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not users.login(username, password):
            return render_template("error.html", message="Wrong username or password")
        return redirect("/")

@app.route("/register", methods = ["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 4:
            return render_template("error.html", message="Username is too short, it should be at least 4 characters long")
        characters = string.ascii_letters + string.digits + "äåöÄÅÖ_"
        for i in username:
            if i not in characters:
                return render_template("error.html", message="Username must have only letters and numbers in it")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="The passwords do not match")
        if len(password1) < 8 or len(password2) < 8:
            return render_template("error.html", message="Password is too short")
        
        if not users.register(username, password1):
            return render_template("error.html", message="The registration was unsuccesful, try a different username")

        return redirect("/")

@app.route("/borrow_books", methods = ["get", "post"])
def borrow_books():
    if request.method == "GET":
        all_books = books.find_all_books()

        return render_template("borrow_books.html", books = all_books)

@app.route("/confirm_books", methods = ["get", "post"])
def confirm_books():
    if request.method == "GET":
        #show what was chosen in borrow_books
        pass

    if request.method == "POST":
        #take chosen books and make borrowings of of them
        pass

@app.route("/add_book", methods = ["get", "post"])
def add_book():
    if request.method == "GET":
        return render_template("add_book.html")
    
    if request.method == "POST":
        name = request.form["name"]
        amount = request.form["amount"]
        if not books.add_books(name, amount):
            return render_template("error.html", message="Adding the book failed, try again")
        
        return redirect("/borrow_books")

@app.route("/logout")
def logout():
    users.logout()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)