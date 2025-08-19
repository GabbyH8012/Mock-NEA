from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def signin():
    return render_template("signin.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/auth/createuser", methods=["POST"])
def createUser():
    formDetails = request.form
    username = formDetails.get("username")
    password = formDetails.get("password")
    repassword = formDetails.get("repassword")

    if len(username) > 2 and len(password) > 7 and len(repassword) > 7:
        return "creating user..."
    

    return "failed to create user..."

app.run(debug = True)