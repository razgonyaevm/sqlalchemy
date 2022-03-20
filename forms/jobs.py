from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    title = StringField("Job Title", validators=[DataRequired()])
    teamleader = StringField("Team Leader id", validators=[DataRequired()])
    size = StringField("Work Size")
    collab = StringField("Collaborators")
    finish = BooleanField("Is job finished?")
    submit = SubmitField("Submit")
