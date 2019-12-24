from app import app, db, bcrypt, mail
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, SignupForm
from app.models import Users, Recipe_Posts
from flask_login import current_user, login_user, login_required
from werkzeug.urls import url_parse
from flask_login import logout_user
from flask_mail import Message
from app.email import confirm_token, generate_confirmation_token, send_email


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('loadHomePage'))


@app.route('/')
def loadHomePage():
    posts = Recipe_Posts.query.all()
    return render_template("home.html", posts=posts)


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
            flash('Mật khẩu hoặc tài khoản không đúng')
            return redirect(url_for('login'))
        elif not user.confirmed:
            flash('Tài khoản của bạn chưa được xác nhận đăng ký!')
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
        newUser.confirmed = False
        db.session.add(newUser)
        db.session.commit()

        token = generate_confirmation_token(newUser.email)
        confirm_url = url_for('user.confirm_email', token=token, _external=True)
        html = render_template('email.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(newUser.email, subject, html)

        flash('Email xác nhận đăng ký tài khoản đã được gửi đến bạn. Hãy kiểm tra và xác nhận!')
        return redirect(url_for('signup'))
    return render_template("signup.html", form=form)


@app.route('/confirm/<token>')
@login_required
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = Users.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('main.home'))


if __name__ == '__main__':
    app.run()
