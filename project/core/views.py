# core/views.py
from flask import render_template, request, redirect, url_for, Blueprint
from project.models import BlogPost
from project.core.forms import SearchForm
from sqlalchemy import or_

core = Blueprint('core', __name__)


# ------------------------------------------------
# home page view --------------------------------
@core.route('/')
def home():

    # get page number from url (default to 1)
    page = request.args.get('page', 1, type=int)

    # get paginated blog posts (newest first)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=6, error_out=False)  # show 6 posts per page

    return render_template('core/home.html', posts=blog_posts)



# ------------------------------------------------
# about page view --------------------------------
@core.route('/about')
def about():
    return render_template('core/about.html')




# ------------------------------------------------
# search page view --------------------------------
@core.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('q', '')

    if form.validate_on_submit():
        # if form was submitted, get search term from form
        search_query = form.search.data
        return redirect(url_for('core.search', q=search_query))

    if search_query:
        results = BlogPost.query.filter(
            or_(
                BlogPost.title.ilike(f'%{search_query}%'),
                BlogPost.text.ilike(f'%{search_query}%'),
                BlogPost.category.ilike(f'%{search_query}%')
            )
        ).order_by(BlogPost.date.desc()).paginate(page=page, per_page=6)
    else:
        results = []

    return render_template('core/search.html', form=form, results=results, search_query=search_query)