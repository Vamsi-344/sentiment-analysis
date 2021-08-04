from flask import render_template, url_for, redirect
from webapp import app, bnb, lgr, svc
from webapp.forms import TweetForm


@app.route("/", methods=['GET', 'POST'])
def home():
	form = TweetForm()
	if form.validate_on_submit():
		if form.classifier.data == 'bn':
			result = bnb.predict([form.tweet.data])
			return render_template('answer.html', result=result, clf='bn')
		elif form.classifier.data == 'lg':
			result = lgr.predict([form.tweet.data])
			return render_template('answer.html', result=result, clf='lg')
		else:
			result = svc.predict([form.tweet.data])
			return render_template('answer.html', result=result, clf='sv')
	return render_template('home.html', form=form)
