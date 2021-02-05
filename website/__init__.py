import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

secret = os.urandom(16)
app.config['SECRET_KEY'] = secret

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# login_manager.init_app(app)
# login_manager.login_view = 'login'

from website.error_pages.handlers import error_pages
from website.portfolio.views import portfolio

app.register_blueprint(error_pages)
app.register_blueprint(portfolio,url_prefix='/portfolio')
