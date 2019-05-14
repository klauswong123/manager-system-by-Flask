from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

bootstrap = Bootstrap(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)