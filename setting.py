from flask import Flask
from flask_bootstrap import Bootstrap
from datetime import timedelta
import random, string, hashlib
from flask_sqlalchemy import SQLAlchemy



n = ''.join(random.sample(string.ascii_letters + string.digits, 32))
m = hashlib.md5()
m.update(n.encode('utf-8'))
result = m.hexdigest()
UPLOAD_FOLDER = 'static/photo'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:pw@/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = result
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
bootstrap = Bootstrap(app)

app.config.from_object(__name__)
db = SQLAlchemy(app)
