# project/users/views.py 

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from project.models import User, BlogPost
from project.users.forms import RegistrationForm, LoginForm, EditAccountForm
from project.users.picture_handler import add_profile_pic
from project import db


# ------------------------------------------------
# blueprint --------------------------------
users = Blueprint('users', __name__)



# ------------------------------------------------
# register view new --------------------------------
@users.route('/signup', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # check if email or username already exists
        email_exists = User.query.filter_by(email=form.email.data).first()
        username_exists = User.query.filter_by(username=form.username.data).first()

        if email_exists:
            flash('This email address is already taken. Please use a different one.', 'danger')
        elif username_exists:
            flash('This username is already taken. Please choose a different one.', 'danger')
        else:
            # create a new user if email and username are unique
            user = User(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                role=form.role.data,
                location=form.location.data,
                email=form.email.data,
                username=form.username.data,
                password=form.password.data
            )

            try:
                db.session.add(user)
                db.session.commit()
                flash('Your account has been created successfully.', 'success')
                return redirect(url_for('users.login'))
            except IntegrityError:
                db.session.rollback()
                flash('An error occurred during registration. Please try again.', 'danger')

    return render_template('users/register.html', form=form)




# ------------------------------------------------
# login view new --------------------------------
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  # find user by email

        if user is None:
            # if no user is found with the provided email
            flash('Email not found. Please check your email or sign up for a new account.', 'danger')
        elif not user.check_password(form.password.data):
            # if the password is incorrect
            flash('Incorrect password. Please try again.', 'danger')
        else:
            # if both email and password are correct
            login_user(user)
            flash(f'Logged in as {user.username}', 'success')  

            # handle the "next" parameter for redirecting after login
            next = request.args.get('next')
            if next is None or not next.startswith('/'):  # ensures "next" is a safe URL
                next = url_for('core.home')
            return redirect(next)

    return render_template('users/login.html', form=form)





# ------------------------------------------------
# logout view --------------------------------
@users.route('/logout')
def logout():
    logout_user()
    flash("You've been logged out.", "info")
    return redirect(url_for('core.home'))





# ------------------------------------------------
# account or profile view new --------------------------------
@users.route('/account')
@login_required
def account():

    return render_template('users/account.html')




# ------------------------------------------------
# edit account view new --------------------------------
@users.route('/edit_account', methods=['GET', 'POST'])
@login_required
def edit_account():
    form = EditAccountForm()

    if form.validate_on_submit():
        # check if the new username already exists (excluding the current user's data)
        username_exists = User.query.filter(User.username == form.username.data, User.id != current_user.id).first()

        if username_exists:
            flash('This username is already taken. Please choose a different one.', 'danger')
        else:
            # update the user's account details
            if form.picture.data:
                username = current_user.username
                pic = add_profile_pic(form.picture.data, username)
                current_user.profile_image = pic

            current_user.first_name = form.first_name.data
            current_user.last_name = form.last_name.data
            current_user.role = form.role.data
            current_user.location = form.location.data
            current_user.username = form.username.data
            current_user.bio = form.bio.data

            # update the password only if a new password is provided
            if form.password.data:
                current_user.password_hash = generate_password_hash(form.password.data)

            db.session.commit()
            flash('Your account information has been saved.', 'success')
            return redirect(url_for('users.account'))

    elif request.method == 'GET':
        # pre-populate the form with the current user's data
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.role.data = current_user.role
        form.location.data = current_user.location
        form.username.data = current_user.username
        form.bio.data = current_user.bio

    # dynamically generate the URL for the current user's profile image
    profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)

    return render_template('users/edit_account.html', profile_image=profile_image, form=form)





# ------------------------------------------------
# delete account view new () --------------------------------

@users.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    try:
        user = current_user._get_current_object()
        logout_user()  # log out before deletion 
        
        db.session.delete(user)
        db.session.commit()
        flash('Your account and all associated blog posts have been permanently deleted.', 'success')
        return redirect(url_for('core.home'))
    
    except Exception as e:
        db.session.rollback()  # rollback if deletion fails
        flash('An error occurred while deleting your account. Please try again.', 'danger')
        print(f"Account deletion error: {str(e)}")  # log the error for debugging
        return redirect(url_for('users.account'))  # redirect back to account page






# ------------------------------------------------
# user blog post list view (not created the template yet) --------------------------------

# @users.route('/<username>')
# def user_posts(username):

#     page = request.args.get('page', 1, type=int)
#     user = User.query.filter_by(username=username).first_or_404()  # research about this user and print(user) later
#     blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
#     return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)




# ------------------------------------------------
# user blog post list view --------------------------------
@users.route('/user/<string:username>')
def user_posts(username):
    user = User.query.filter_by(username=username).first_or_404()
    # get paginated posts for this user
    page = request.args.get('page', 1, type=int)
    posts = BlogPost.query.filter_by(author=user)\
               .order_by(BlogPost.date.desc())\
               .paginate(page=page, per_page=6)
    return render_template('users/user_posts.html', posts=posts, user=user)