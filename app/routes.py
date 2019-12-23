from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, SignupForm
from app.models import Users

@app.route('/')
def loadHomePage():
    return render_template("home.html")

@app.route('/addnewpost')
def loadAddNewPost():
    return render_template("writerecipe.html")

@app.route('/signin', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('index'))
    form = LoginForm()
    print(Users.query.all())
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', form=form)

@app.route('/signup')
def signup():
    form = SignupForm()
    print(form.gender)
    return render_template("signup.html", form=form)


if __name__ == '__main__':
    app.run()
