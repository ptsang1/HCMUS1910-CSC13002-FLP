from wtforms.fields.html5 import DateField
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import Users, Genders


class LoginForm(FlaskForm):
    username = StringField('<i class="zmdi zmdi-account material-icons-name"></i>',
                           validators=[DataRequired(message="Vui lòng nhập email")])
    password = PasswordField('<i class="zmdi zmdi-lock"></i>',
                             validators=[DataRequired(message="Vui lòng nhập mật khẩu")])
    remember_me = BooleanField('<span></span>Ghi nhớ đăng nhập')
    submit = SubmitField("Đăng nhập")


class SignupForm(FlaskForm):
    fullname = StringField('<i class="zmdi zmdi-account material-icons-name"></i>',
                           validators=[DataRequired(message="Vui lòng nhập họ và tên")])
    email = StringField('<i class="zmdi zmdi-email"></i>',
                        validators=[DataRequired(message="Vui lòng nhập email"),
                                    Email(message="Vui lòng nhập email"),
                                    Length(min=8, max=50)])
    password = PasswordField('<i class="zmdi zmdi-lock"></i>',
                             validators=[DataRequired(message="Vui lòng nhập mật khẩu")])
    confpassword = PasswordField('<i class="zmdi zmdi-lock-outline"></i>',
                                 validators=[DataRequired(message="Vui lòng xác nhận lại mật khẩu"),
                                             EqualTo('password', message="Mật khẩu xác nhận chưa khớp với mật khẩu")])
    birthday = DateField('<i class="zmdi zmdi-cake"></i>', format='%Y-%m-%d',
                         validators=[DataRequired(message="Vui lòng nhập ngày sinh của bạn")])
    choices = [(gender.genderid, gender.gendername) for gender in Genders.query.all()]
    choices.insert(0, ('', 'Giới tính'))
    gender = SelectField('<i class="zmdi zmdi-male-female"></i>', choices=choices, coerce=bool,
                         validators=[DataRequired("Vui lòng chọn giới tính của bạn")])
    submit = SubmitField("Đăng ký")

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email này đã được đăng ký')
