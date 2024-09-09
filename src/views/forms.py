from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators


class BaseForm(FlaskForm):
    class Meta:
        csrf = False


class RegisterForm(BaseForm):
    username = StringField(
        "username",
        validators=[validators.DataRequired(), validators.Length(max=20)],
    )
    email = StringField(
        "email", validators=[validators.DataRequired(), validators.Email()]
    )
    password = StringField("password", validators=[validators.DataRequired()])
    confirm = StringField(
        "confirm",
        validators=[validators.DataRequired(), validators.EqualTo("password")],
    )
    invitation = StringField(
        "invitation", validators=[validators.DataRequired()]
    )


class LoginForm(BaseForm):
    email = StringField(
        "email", validators=[validators.DataRequired(), validators.Email()]
    )
    password = StringField("password", validators=[validators.DataRequired()])


class DeleteForm(BaseForm):
    id = StringField("id", validators=[validators.DataRequired()])
    username = StringField(
        "username",
        validators=[validators.DataRequired(), validators.Length(max=20)],
    )
    email = StringField(
        "email", validators=[validators.DataRequired(), validators.Email()]
    )
    password = StringField("password", validators=[validators.DataRequired()])
