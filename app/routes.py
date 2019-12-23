from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, SignupForm
from app.models import Users
from flask_login import current_user, login_user
from app import db, bcrypt
# from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse

@app.route('/')
def loadHomePage():
    return render_template("home.html")

@app.route('/addnewpost')
def loadAddNewPost():
    return render_template("writerecipe.html")

@app.route('/signin', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('loadHomePage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('loadHomePage')
        return redirect(next_page)
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('loadHomePage'))
    form = SignupForm()
    if form.validate_on_submit():
        newUser = Users()
        newUser.userid = bcrypt.generate_password_hash(form.email.data)
        newUser.email = form.email.data
        newUser.set_password(form.password.data)
        newUser.set_userID(newUser.email)
        newUser.fullname = form.fullname.data
        newUser.roleid = 1
        newUser.genderid = form.gender.data
        newUser.birthday = form.birthday.data
        newUser.avatarlink = ""
        db.session.add(newUser)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template("signup.html", form=form)


if __name__ == '__main__':
    app.run()
