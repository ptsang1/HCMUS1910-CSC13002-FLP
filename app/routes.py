from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
def loadHomePage():
    return render_template("home.html")

@app.route('/addnewpost')
def loadAddNewPost():
    return render_template("writerecipe.html")

@app.route('/signin', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', form=form)

@app.route('/signup')
def signup():
    return render_template("signup.html")


if __name__ == '__main__':
    app.run()
