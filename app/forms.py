from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField
class LoginForm(FlaskForm):
    username = StringField('<i class="zmdi zmdi-account material-icons-name"></i>', validators=[DataRequired()])
    password = PasswordField('<i class="zmdi zmdi-lock"></i>', validators=[DataRequired()])
    remember_me = BooleanField('<span></span>Ghi nhớ đăng nhập')
    submit = SubmitField("Đăng nhập")

class SignupForm(FlaskForm):
    fullname = StringField('<i class="zmdi zmdi-account material-icons-name"></i>', validators=[DataRequired()])
    email = StringField('<i class="zmdi zmdi-email"></i>', validators=[DataRequired()])
    password = PasswordField('<i class="zmdi zmdi-lock"></i>', validators=[DataRequired()])
    confpassword = PasswordField('<i class="zmdi zmdi-lock-outline"></i>', validators=[DataRequired()])
    birthday = DateField('<i class="zmdi zmdi-cake"></i>', format='%dd/%mm/%YYYY', validators=[DataRequired()])
    gender = SelectField('<i class="zmdi zmdi-male-female"></i>', choices=[(1, 'Nam'), (0, 'Nữ')], validators=[DataRequired()])
    submit = SubmitField("Đăng ký")
