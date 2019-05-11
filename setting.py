from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_script import Manager
from flask_bootstrap import Bootstrap
from datetime import timedelta
import random, string, hashlib

n = ''.join(random.sample(string.ascii_letters + string.digits, 32))
m = hashlib.md5()
m.update(n.encode('utf-8'))
result = m.hexdigest()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1314wang@127.0.0.1/jewelry_account"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = result
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
bootstrap = Bootstrap(app)

app.config.from_object(__name__)
db = SQLAlchemy(app)