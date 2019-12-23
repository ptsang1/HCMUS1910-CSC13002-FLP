from wtforms.fields.html5 import DateField
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import Users, Genders

class LoginForm(FlaskForm):
    username = StringField('<i class="zmdi zmdi-account material-icons-name"></i>', validators=[DataRequired(), Email()])
    password = PasswordField('<i class="zmdi zmdi-lock"></i>', validators=[DataRequired()])
    remember_me = BooleanField('<span></span>Ghi nhớ đăng nhập')
    submit = SubmitField("Đăng nhập")

class SignupForm(FlaskForm):
    fullname = StringField('<i class="zmdi zmdi-account material-icons-name"></i>', validators=[DataRequired()])
    email = StringField('<i class="zmdi zmdi-email"></i>', validators=[DataRequired(), Email(), Length(min=8, max=50)])
    password = PasswordField('<i class="zmdi zmdi-lock"></i>', validators=[DataRequired()])
    confpassword = PasswordField('<i class="zmdi zmdi-lock-outline"></i>', validators=[DataRequired(), EqualTo('password')])
    birthday = DateField('<i class="zmdi zmdi-cake"></i>', format='%Y-%m-%d', validators=[DataRequired()])
    choices = [(gender.genderid, gender.gendername) for gender in Genders.query.all()]
    choices.insert(0, ('', 'Giới tính'))
    gender = SelectField('<i class="zmdi zmdi-male-female"></i>', choices=choices, coerce=bool, validators=[DataRequired()])
    submit = SubmitField("Đăng ký")

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
