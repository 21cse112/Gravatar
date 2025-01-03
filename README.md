# Gravatar Profile Display: Personalized User Cards with Flask

This Flask-based web application allows users to submit their profile information and retrieves Gravatar data based on their email. It dynamically displays a detailed profile card, including the user's photo, bio, location, and contact details. If Gravatar data is missing, the form inputs serve as a fallback.

## Features
- **Profile Form**: Collects email, full name, username, phone, location, bio, and website.
- **Gravatar Integration**: Fetches profile image, username, location, and bio using the email.
- **Profile Card UI**: Displays collected data with a clean layout, including profile image, personal details, contact info, bio, and clickable website.

## Technologies Used
- **Flask**: Web framework
- **HTML/CSS**: Frontend
- **Gravatar API**: User profile data

## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```

4. Open `http://127.0.0.1:5000/` in your browser.
