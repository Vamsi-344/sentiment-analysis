from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class TweetForm(FlaskForm):
    tweet = StringField('Tweet', validators=[DataRequired(), Length(min=2, max=100)])
    classifier = SelectField('Select a classifier..', choices=[('bn', 'BernoulliNB'), ('lg', 'LogisticRegression'), ('sv', 'SVM')])
    submit = SubmitField('Check!')