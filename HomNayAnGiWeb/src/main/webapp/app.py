from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def loadHomePage():
    return render_template("home.html")

@app.route('/addnewpost')
def loadAddNewPost():
    return render_template("writerecipe.html")

@app.route('/signin')
def loadSigninPage():
    return render_template("login.html")

@app.route('/signup')
def loadSignupPage():
    return render_template("signup.html")

if __name__ == '__main__':
    app.run()
