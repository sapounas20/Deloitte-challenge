# CMS DELLOITTE CHALLENGE
This is a CMS programm for the deloitte challenge


To upload an image, FIRST create an uload folder

## Features

- **User Authentication**: Admins can log in using a username and password to receive an authentication token.
- **Role-based Access**: Admins can create, update, and delete articles and images, while guests can only view content.
- **Article Management**: Admins can create, edit, delete, and retrieve articles.
- **Image Management**: Admins can upload images and associate them with articles.
- **REST API**: Provides endpoints for all operations, with responses in JSON format.
- **File Uploads**: Images are securely uploaded using `secure_filename` and stored on the server.

## Technologies

- **Flask**: Python microframework used to create the REST API.
- **Flask-JWT-Extended**: Used for handling JWT-based authentication.
- **Flask-SQLAlchemy**: Object-Relational Mapping (ORM) for interacting with the database.
- **SQLite**: The default relational database used in development.
- **Flask-Smorest**: For generating REST API endpoints and Swagger documentation.
- **Werkzeug**: Utility for handling file uploads securely.

## Requirements

Ensure that you have the following installed:

- Python 3.9 or above
- Virtualenv (optional but recommended)
- Flask and other Python dependencies (listed in `requirements.txt`)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/flask-cms.git
   cd flask-cms

## Installation

2. **Create a virtual environment (optional but recommended):**

   ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Set up the database:**
    ```bash
    flask db init
    flask db migrate
    flask db upgrade

## Running the app

1. **Run the Flask development server:**
    ```bash
    flask run
The application will be available at http://localhost:5001.

2. **Swagger API Documentation:**
You can access the API documentation at http://localhost:5001/swagger-ui.


