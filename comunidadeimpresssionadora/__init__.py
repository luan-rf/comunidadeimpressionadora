from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '83ce53d771f2fadb93c2ad7f1e6f07b4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcript = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_criarconta'
login_manager.login_message_category= 'alert-info'


from comunidadeimpresssionadora import routes