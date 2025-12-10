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

  **Sign Up Page:**
<br>
  User registration form with unique username and email validation.

<img width="600" height="578" alt="Image" src="https://github.com/user-attachments/assets/78439658-78ac-4fc8-ae3f-d05c813c3f1a" />
<br><br>


  **Create New Blog Post:**
<br>
  Blog creation form featuring category selection and image upload support.

<img width="600" height="826" alt="Image" src="https://github.com/user-attachments/assets/8b3a10e3-8e40-40db-9a69-0df196b34820" />
<br><br>


  **Single Blog Post View:**
<br>
  Displays the full blog post with edit/delete controls for the authenticated author.

  <img width="600" height="896" alt="Image" src="https://github.com/user-attachments/assets/0c7896c4-e079-4654-a22e-9b204e6e32e6" />
<br><br>


  **Delete Confirmation Modal:**
<br>
  A confirmation popup asking the author to verify before deleting a post.

  <img width="600" height="496" alt="Image" src="https://github.com/user-attachments/assets/1394282f-0a46-4b11-b3ab-f0ff004eb3d1" />
<br><br>


  **Category Filter Page:**
<br>
  Lists all posts under a selected category with pagination for smooth navigation.

  <img width="600" height="782" alt="Image" src="https://github.com/user-attachments/assets/3037f991-e983-450e-9094-5bc76012c40b" />
<br><br>


  **User Blogs Page:**
<br>
  Shows all blog posts written by a specific user.

  <img width="600" height="1356" alt="Image" src="https://github.com/user-attachments/assets/925e9910-6214-4c41-9cc7-3117115a9e69" />
<br><br>


  **Search Results Page:**
<br>
  Displays posts matching the search query across titles, content, and categories.

  <img width="600" height="1007" alt="Image" src="https://github.com/user-attachments/assets/3d031490-0aae-48ec-9247-9df1d1c26f83" />
<br><br>


  **User Profile Page:**
<br>
  Shows user details with a default avatar, plus options to update the profile or log out.

  <img width="600" height="504" alt="Image" src="https://github.com/user-attachments/assets/86f5ecba-76c3-4be5-a666-b312a3c181c1" />
<br><br>


  **Edit Profile Page:**
<br>
  Form to update account information with an optional delete-account action.

  <img width="600" height="688" alt="Image" src="https://github.com/user-attachments/assets/366f7a3e-1d23-43ab-a90d-7326b24169dc" />
  <br>



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
   