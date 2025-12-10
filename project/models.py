from project import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime, timezone



# login manager 
@login_manager.user_loader  
def load_user(user_id):
    return User.query.get(user_id)




# user model 
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    role = db.Column(db.String(64), nullable=False)  
    location = db.Column(db.String(64), nullable=False) 
    profile_image = db.Column(db.String(64), nullable=False, default='default_img.jpg')
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    bio = db.Column(db.Text, nullable=True)
    account_created = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    

    posts = db.relationship('BlogPost', backref='author', lazy=True, cascade="all, delete")  # relationship 


    def __init__(self, first_name, last_name, role, location, email, username, password, bio=None):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.location = location
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.bio = bio

    def check_password(self, password): 
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'Username: {self.username}, Name: {self.first_name} {self.last_name}'
    


    

# blog_Post model 
class BlogPost(db.Model):
    __tablename__ = 'blog_posts'  # explicit table name

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    date_updated = db.Column(db.DateTime, nullable=True)
    title = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    cover_image = db.Column(db.String(64), nullable=False)
    category = db.Column(db.String(64), nullable=False)


    def __init__(self, title, text, user_id, cover_image, category):
        self.title = title
        self.text = text
        self.user_id = user_id
        self.cover_image = cover_image
        self.category = category
    
    def __repr__(self):
        return f'Post ID - {self.id}, date - {self.date}, last updated - {self.date_updated}, title - {self.title}, category - {self.category}'