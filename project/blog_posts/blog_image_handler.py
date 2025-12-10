# project/blog_posts/blog_image_handler.py
import os
from PIL import Image, UnidentifiedImageError
from flask import current_app
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def add_blog_cover_image(pic_upload, blog_id):
    filename = secure_filename(pic_upload.filename)
    ext_type = filename.split('.')[-1].lower()

    if ext_type not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Invalid file extension. Allowed: {ALLOWED_EXTENSIONS}")

    storage_filename = f"blog_cover_{blog_id}.jpg"  # force JPEG
    upload_folder = os.path.join(current_app.root_path, 'static/blog_cover_images')
    
    # create the upload folder if it doesn't exist
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    filepath = os.path.join(upload_folder, storage_filename)
    output_size = (1200, 800)
    
    try:
        pic = Image.open(pic_upload)
        # process image
        pic.thumbnail(output_size)
        pic = pic.convert('RGB')
        pic.save(filepath, optimize=True, quality=90)
    except UnidentifiedImageError:
        raise ValueError("Invalid image file")
    except Exception as e:
        raise ValueError(f"Image processing error: {str(e)}")

    return storage_filename