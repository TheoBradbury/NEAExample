from flask import Flask, redirect, render_template, request, url_for, session
from database import DatabaseHandler

app = Flask(__name__)

@app.route("/")
def home(): 
    return render_template("home.html")

@app.route("/dashboard")
def dashboard(): 
    return "dis the dash"

@app.route("/login")
def login(): 
    return render_template("signin.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/auth/createuser", methods=["POST"]) 
def createuser():
    formDetails = request.form
    print(formDetails)

    user = formDetails.get("username")
    password = formDetails.get("password")
    repass = formDetails.get("repassword")


    print(user)

    if password == repass:
        db = DatabaseHandler()
        if db.createUser(user, password): 
            return redirect(url_for("dashboard"))
        else:
            return redirect(url_for("signup"))
    
    return "passwords do not match" 


@app.route("/auth/login", methods=["POST"])
def authLogin():
    formDetails = request.form 
    print(formDetails)
    user = formDetails.get("username")
    password = formDetails.get("password")
    print(user)

    db = DatabaseHandler()
    result = db.loginUser(user, password)
    if result:
        session["currentUser"] = user 
        return redirect(url_for("dashboard"))
    else: 
        return redirect(url_for("login"))
        


app.run(debug = True)