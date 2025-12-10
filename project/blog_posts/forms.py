# project/blog_posts/forms.py 
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField, SelectField, RadioField
from wtforms.validators import DataRequired, InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.widgets import RadioInput, ListWidget


# blog post form --------------------------------
class BlogPostForm(FlaskForm):

    CATEGORIES = [
        ('travel', 'Travel'),
        ('photography', 'Photography'),
        ('art', 'Art'),
        ('books', 'Books'),
        ('sports', 'Sports'),
        ('hobbies', 'Hobbies'),
        ('pets', 'Pets'),
        ('food', 'Food'),
        ('fashion', 'Fashion'),
        ('health', 'Health'),
        ('lifestyle', 'Lifestyle'),
        ('philosophy', 'Philosophy'),
        ('spirituality', 'Spirituality'),
        ('home', 'Home'),
        ('relationships', 'Relationships'),
        ('family', 'Family'),
        ('education', 'Education'),
        ('career', 'Career'),
        ('finance', 'Finance'),
        ('technology', 'Technology'),
        ('lifestyle', 'Lifestyle'),
        ('business', 'Business'),
        ('automotive', 'Automotive'),
        ('gaming', 'Gaming'),
        ('movies', 'Movies'),
        ('music', 'Music'),
        ('news', 'News'),
        ('society', 'Society'),
        ('charity', 'Charity'),
    ]

    title = TextAreaField('Blog Title *', validators=[DataRequired()], render_kw={"rows": 2})
    text = TextAreaField('Blog Content *', validators=[DataRequired()])
    blog_image = FileField('Blog Cover Image (JPG, JPEG, or PNG only) *', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    
    category = RadioField(
        'Select One Category *',
        choices=CATEGORIES,
        validators=[DataRequired()],
        widget=ListWidget(prefix_label=False), 
        option_widget=RadioInput() 
    )
    
    submit = SubmitField('Post')