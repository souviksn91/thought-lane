# app.py
from project import app, db
from project.models import User, BlogPost  # import models

# create tables if they don't exist
with app.app_context():
    db.create_all()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=False)

# having issues with mac, so changed the port to 8000
if __name__ == '__main__':
    app.run(debug=True, port=8000)
