import pickle
from flask import Flask 

with open(f'models/text_sentiment_analysis_bnb.pkl', 'rb') as f:
	bnb = pickle.load(f)

with open(f'models/text_sentiment_analysis_lgr.pkl', 'rb') as f:
	lgr = pickle.load(f)

with open(f'models/text_sentiment_analysis_svc.pkl', 'rb') as f:
	svc = pickle.load(f)

app = Flask(__name__)
app.config['SECRET_KEY'] = '4c43954c0bb9a7e21a2236782e1d2fe6'

from webapp import routes
