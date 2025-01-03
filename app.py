from flask import Flask, render_template, request
import hashlib
import requests

app = Flask(__name__)

# Default path for the placeholder image
DEFAULT_AVATAR = "static/images/placeholder.png"

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    email = request.form.get("email")
    name = request.form.get("name")
    username = request.form.get("username")
    phone = request.form.get("phone")
    location = request.form.get("location")
    bio = request.form.get("bio")
    website = request.form.get("website")

    # Generate Gravatar hash using the email for api request
    email_hash = hashlib.md5(email.strip().lower().encode()).hexdigest()
    gravatar_url = f"https://gravatar.com/{email_hash}.json"

    # Fetch Gravatar data
    gravatar_data = {}
    try:
        response = requests.get(gravatar_url)
        if response.status_code == 200:
            gravatar_data = response.json()
    except Exception as e:
        print(f"Error fetching Gravatar data: {e}")

    
    display_name = (
        gravatar_data["entry"][0].get("displayName") if gravatar_data.get("entry") else name
    )
    profile_image_url = (
        gravatar_data["entry"][0]["photos"][0]["value"]
        if gravatar_data.get("entry") and gravatar_data["entry"][0].get("photos")
        else DEFAULT_AVATAR
    )
    profile_location = (
        gravatar_data["entry"][0].get("currentLocation") if gravatar_data.get("entry") else location
    )
    profile_bio = (
        gravatar_data["entry"][0].get("aboutMe") if gravatar_data.get("entry") else bio
    )

    return render_template(
        "index.html",
        display_name=display_name,
        email=email,
        username=username,
        phone=phone,
        location=profile_location,
        bio=profile_bio,
        website=website,
        profile_image_url=profile_image_url,
    )

if __name__ == "__main__":
    app.run(debug=True)
