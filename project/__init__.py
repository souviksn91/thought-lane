# project/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_login import LoginManager

# load environment variables
load_dotenv()

app = Flask(__name__)

# app.config['SECRET_KEY'] = 'mykey'  # OLD

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB limit


basedir = os.path.abspath(os.path.dirname(__file__))


db = SQLAlchemy(app)
Migrate(app,db)


# loginmanager setup --------------------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


# blueprints setup --------------------------------
from project.core.views import core
from project.users.views import users
from project.blog_posts.views import blog_posts
from project.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)
