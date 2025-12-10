# The Thought Lane – A Blogging Platform Built With Flask & MySQL
The Thought Lane is a feature-rich blogging platform built using Flask, MySQL, and SQLAlchemy.
It allows users to create accounts, write blogs, upload cover images, browse posts by categories, search content, and manage their own profiles — all wrapped in a clean and minimalist UI.

<img width="1863" height="1605" alt="Image" src="https://github.com/user-attachments/assets/a4884a7d-251d-4031-b9b9-562abdd5e30f" />

## Features
- Create, view, update, and delete blog posts
- User authentication with signup and login
- Category filtering to browse posts by interest
- Search posts by title, content, or category
- Pagination for browsing posts smoothly
- User profile page with editable account details and avatar placeholder
- Clean UI with a focus on readability and a pleasant writing experience

## Technologies
- **Backend:** Python, Flask, SQLAlchemy
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** MySQL

<hr>

## Screenshots

- **Sign Up Page**
<br>
  User registration form with unique username and email validation.

  <img width="803" height="773" alt="Image" src="https://github.com/user-attachments/assets/49385475-3e11-4e93-b2b0-75bfe5bf583d" />
<br><br>


- **Create New Blog Post**
<br>
Blog creation form featuring category selection and image upload support.

  <img width="818" height="1126" alt="Image" src="https://github.com/user-attachments/assets/acabc2c1-a299-49c4-adca-e36bcd147ef3" />
<br><br>


- **Single Blog Post View**
<br>
Displays the full blog post with edit/delete controls for the authenticated author.

  <img width="797" height="1190" alt="Image" src="https://github.com/user-attachments/assets/defb37fe-3c9c-4b9b-87f0-467b74fc1469" />
<br><br>


- **Delete Confirmation Modal**
<br>
A confirmation popup asking the author to verify before deleting a post.

  <img width="801" height="662" alt="Image" src="https://github.com/user-attachments/assets/ec57cd1a-b7d3-40d2-bd35-a56da6a07044" />
<br><br>


- **Category Filter Page**
<br>
Lists all posts under a selected category with pagination for smooth navigation.

  <img width="804" height="1044" alt="Image" src="https://github.com/user-attachments/assets/935c97f8-287d-4d23-ae9f-d4c6898dda55" />
<br><br>


- **User Blogs Page**
<br>
Shows all blog posts written by a specific user.

  <img width="843" height="1905" alt="Image" src="https://github.com/user-attachments/assets/e61314c0-be69-4eb7-ab33-8732277553e1" />
<br><br>


- **Search Results Page**
<br>
Displays posts matching the search query across titles, content, and categories.

  <img width="812" height="1362" alt="Image" src="https://github.com/user-attachments/assets/8762f089-9ea9-4ddd-8f94-ecf2521f23e3" />
<br><br>


- **User Profile Page**
<br>
Shows user details with a default avatar, plus options to update the profile or log out.

  <img width="845" height="712" alt="Image" src="https://github.com/user-attachments/assets/fa796feb-efde-4540-ab06-f7d4ea6f1e9f" />
<br><br>


- **Edit Profile Page**
<br>
Form to update account information with an optional delete-account action.

  <img width="854" height="980" alt="Image" src="https://github.com/user-attachments/assets/e8d89731-10a6-4c83-a353-7b98cf0a8cfe" />



<hr>

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/souviksn91/pycontacts.git
   cd pycontacts
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database:**
    Create a new database in MySQL and update the credentials in your .env file (refer to DATABASE.md for detailed steps.)

5. **Run the app:**
   ```bash
   python app.py
   ```
6. **Access in browser:**
   http://127.0.0.1:5000/
   