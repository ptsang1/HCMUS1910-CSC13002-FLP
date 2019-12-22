from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('<i class="zmdi zmdi-account material-icons-name"></i>', validators=[DataRequired()])
    password = PasswordField('<i class="zmdi zmdi-lock"></i>', validators=[DataRequired()])
    remember_me = BooleanField('<span></span>Ghi nhớ đăng nhập')
    submit = SubmitField("Đăng nhập")
