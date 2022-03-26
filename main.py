
from flask import Flask, render_template, request, redirect, flash, url_for, session, logging
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt 

app = Flask(__name__)
db = app.config["MONGO_URI"] = "mongodb://localhost:27017/wad"
app.config['SECRET_KEY']='thisisanauthenticationapp'
mongo = PyMongo(app)
auth = HTTPBasicAuth()


# 1.2 Render authentication form at http://localhost:5000/
@app.route("/",methods=["GET", "POST"])
#@auth.login_required
def index():
    if request.method == "GET":
        return render_template("login.html", username="", password="")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        print(username)
        print(password)
        if mongo.db.users.find_one({"username": username, "password": password}):
            return redirect(url_for('profile'))
        else:
            return render_template("failed.html")

    
    
#1.3 Redirect user to profile page if successfully authenticated
#return "Hello, %s!" % auth.username()

#1.4 Show profile page for authenticated user only at http://localhost:5000/profile
@app.route("/profile")
def profile():
    return render_template("cv.html")

#1.5 User name and password are stored in Mongodb


#1.1 Listen on localhost:5000
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)