# project/blog_posts/views.py 
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import current_user, login_required
from project.models import BlogPost
from project.blog_posts.forms import BlogPostForm
from project import db
from project.blog_posts.blog_image_handler import add_blog_cover_image
from datetime import datetime, timezone


# ------------------------------------------------
# blueprint --------------------------------
blog_posts = Blueprint('blog_posts', __name__)



# ------------------------------------------------
# create post view new -------------------------------- 
@blog_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():

    form = BlogPostForm()

    if form.validate_on_submit():
        print("Form validated successfully!")  # debug statement

        if form.blog_image.data:
            try:
                # create the blog post without the cover image initially
                blog_post = BlogPost(
                    title=form.title.data,
                    text=form.text.data,
                    user_id=current_user.id,
                    cover_image='',  # temporarily empty
                    category=form.category.data  # add category
                )

                print("BlogPost object created:", blog_post)  # debug statement

                db.session.add(blog_post)
                db.session.commit()  # commit to get the blog_post.id

                print("BlogPost committed to database. ID:", blog_post.id)  # debug statement

                # process the cover image
                try:
                    cover_image_filename = add_blog_cover_image(form.blog_image.data, blog_post.id)
                    print("Cover image processed. Filename:", cover_image_filename)  # debug statement
                    blog_post.cover_image = cover_image_filename
                    db.session.commit()  # commit again to update the cover_image field
                    flash('Blog post created successfully!', 'success')
                    return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post.id))
                
                except ValueError as e:  # specific image errors
                    db.session.rollback()
                    flash(str(e), 'danger')
                    
                except Exception as e:  # other errors
                    db.session.rollback()
                    flash(f'Image processing failed: {str(e)}', 'danger')


            except Exception as e:  # general post creation error 
                db.session.rollback()  
                flash(f'An error occurred: {str(e)}', 'danger')
                print("Error:", str(e))  # debug statement
        else:
            flash('Cover image is required.', 'danger')
    else:
        print("Form validation failed. Errors:", form.errors)  # debug statement

    return render_template('blog_posts/create_post.html', form=form)





# ------------------------------------------------
# single blog post view --------------------------------
@blog_posts.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_posts/blog_post.html', post=blog_post)




# ------------------------------------------------
# update blog post view --------------------------------
@blog_posts.route('/update/<int:blog_post_id>', methods=['GET', 'POST'])
@login_required
def update_post(blog_post_id):
    # fetch the blog 
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    # ensure the current user is the author of the blog post
    if blog_post.author != current_user:
        flash('You are not authorized to update this post.', 'danger')
        return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post.id))

    # initialize the form
    form = BlogPostForm()

    if form.validate_on_submit():
        print("Form validated successfully!")  # debug statement
        try:
            # track if any changes are made
            changes_made = False

            # check if the title has changed
            if blog_post.title != form.title.data:
                blog_post.title = form.title.data
                changes_made = True

            # check if the text has changed
            if blog_post.text != form.text.data:
                blog_post.text = form.text.data
                changes_made = True

            if blog_post.category != form.category.data:
                blog_post.category = form.category.data
                changes_made = True
                print(f"Category changed to: {form.category.data}")

            # check if a new cover image is uploaded
            if form.blog_image.data:
                try:
                    cover_image_filename = add_blog_cover_image(form.blog_image.data, blog_post.id)
                    blog_post.cover_image = cover_image_filename
                    changes_made = True
                except ValueError as e:  # image-specific errors
                    flash(str(e), 'danger')
                except Exception as e:
                    flash(f'Image update failed: {str(e)}', 'danger')


            # update date_updated only if changes are made
            if changes_made:
                blog_post.date_updated = datetime.now(timezone.utc)
                flash('Blog post updated successfully!', 'success')
            else:
                flash('No changes were made to the blog post.', 'info')

            # commit changes to the database
            db.session.commit()
            return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post.id))

        except Exception as e:  # for general errors
            db.session.rollback()  
            flash(f'An error occurred: {str(e)}', 'danger')
            print("Error:", str(e))  # debug statement
    else:
        print("Form validation failed. Errors:", form.errors)  # debug statement

    # pre-fill the form with existing data
    form.title.data = blog_post.title
    form.text.data = blog_post.text
    form.category.data = blog_post.category 

    # Render the template with is_update=True
    return render_template('blog_posts/create_post.html', form=form, is_update=True)




# ------------------------------------------------
# delete blog post view --------------------------------
@blog_posts.route('/delete/<int:blog_post_id>', methods=['POST'])
@login_required
def delete_post(blog_post_id):
    # fetch the blog post to be deleted
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    # ensure the current user is the author of the blog post
    if blog_post.author != current_user:
        flash('You are not authorized to delete this post.', 'danger')
        return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post.id))

    try:
        # delete the blog post from the database
        db.session.delete(blog_post)
        db.session.commit()
        flash('Blog post deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # rollback in case of an error
        flash(f'An error occurred while deleting the post: {str(e)}', 'danger')
        print("Error:", str(e))  # debug statement

    # redirect to the home page or blog list page after deletion
    return redirect(url_for('core.home'))  




# ------------------------------------------------
# category specific blog post view --------------------------------
@blog_posts.route('/category/<category_slug>')
def category_posts(category_slug):
    # get human-readable category name to disply on the page
    category_name = "Uncategorized"
    for slug, name in BlogPostForm.CATEGORIES:
        if slug == category_slug:
            category_name = name
            break

    # get paginated posts
    posts = BlogPost.query.filter_by(category=category_slug).order_by(BlogPost.date.desc())
    total_posts = posts.count()
    
    page = request.args.get('page', 1, type=int)
    # paginate after counting
    posts = posts.paginate(page=page, per_page=5)
    
    return render_template('blog_posts/category_posts.html', posts=posts, total_posts=total_posts, category_name=category_name, category_slug=category_slug)