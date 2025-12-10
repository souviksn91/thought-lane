# project/users/picture_handler.py
import os
from PIL import Image, UnidentifiedImageError
from flask import current_app
from werkzeug.utils import secure_filename

# allowed file extensions for profile pictures
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def add_profile_pic(pic_upload, username):
    filename = secure_filename(pic_upload.filename)
    ext_type = filename.split('.')[-1].lower()

    if ext_type not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Invalid file extension. Allowed: {ALLOWED_EXTENSIONS}")

    storage_filename = f"{secure_filename(username)}.jpg"  # force JPEG
    upload_folder = os.path.join(current_app.root_path, 'static/profile_pics')
    
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    filepath = os.path.join(upload_folder, storage_filename)
    output_size = (400, 400)
    
    try:
        pic = Image.open(pic_upload)
        # process the image
        pic.thumbnail(output_size)
        pic = pic.convert('RGB')
        pic.save(filepath, optimize=True, quality=90)
    except UnidentifiedImageError:
        raise ValueError("Invalid image file")
    except Exception as e:
        raise ValueError(f"Image processing error: {str(e)}")

    return storage_filename