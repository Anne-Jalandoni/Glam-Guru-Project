"""Server for make up reccommendation app."""

from flask import Flask, render_template,request, redirect, session, url_for,jsonify
#from flask_socketio import SocketIO
from crud import create_user, get_users, get_user_by_id,authenticate_user,create_color,get_colors,get_color_by_id,create_product,get_products,get_product_by_id,search_products_by_color,create_rating, get_ratings, get_rating_by_id, add_profile_pic
from model import connect_to_db, db, User, Quiz, Color, Product, Rating
import cloudinary
import cloudinary.uploader
import os
import cv2
import numpy as np
import requests



#ADD PICTURES AND DATA TO LIBRARY
#ADD MAKE UP RECOMMENDATION TO USER PROFILE
#ADD SEARCH/FILTER BUTTON TO HOMEPAGE
#FIX CSS AND STYLING/ DO BOOTSTRAP TEMPLATE
#DO NOT FORGET ABOUT BASE INHERITANCE(REQUIREMENT!!!) - 1-2 Jinja templates that use template inheritance
#DO NOT FORGET TO STORE SECRETS IN GITIGNORE!!!
#One feature that uses JavaScript to manipulate the DOM
#One AJAX request (done)
#IMPLEMENT DELETE
#insert swatches when describing skin tone ("paint chips")

# Mock dataset of products
mock_products = [
    {
        "name": "Foundation A",
        "skin_tones": ["Light", "Medium"],
    },
    {
        "name": "Lipstick B",
        "skin_tones": ["All"],
        # Other product information...
    }
]



app = Flask(__name__)
#place this inside secret.sh
app.secret_key = "SASUKELOVESYOU"  # Change this to a long, random string for better security
#socketio = SocketIO(app)


CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
CLOUD_NAME= "ddslqlvhf" 



# The homepage route
@app.route("/")
def index():
    """Homepage route."""

    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """User registration route."""

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        fname = request.form["fname"]
        lname = request.form["lname"]

        # Retrieve the quiz answers from the session
        quiz_question_1 = session.get("quiz_question_1")
        quiz_question_2 = session.get("quiz_question_2")
        quiz_question_3 = session.get("quiz_question_3")

        # Create the user in the database with quiz answers and registration details
        create_user(email, password, fname, lname, quiz_question_1, quiz_question_2, quiz_question_3)

        # Redirect the user to the login page after successful registration
        return redirect("/login")

    return render_template("register.html")

#The login route
@app.route("/login", methods=["GET", "POST"])
def login():
    """User login route."""

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Authenticate the user (check_password_hash is handled in the authenticate_user function)
        user = authenticate_user(email, password)

        if user:
            # Store the user's id in the session to maintain their login status
            session["user_id"] = user.user_id

            # Redirect the user to their profile page after successful login
            return redirect("/profile")

        # If authentication fails, display an error message or redirect back to the login page
        error_message = "Invalid email or password. Please try again."
        return render_template("login.html", error_message=error_message)

    return render_template("login.html")

#The logout route
@app.route("/logout")
def logout():
    """User logout route."""

    # Remove the user_id from the session to log the user out
    session.pop("user_id", None)

    # Redirect the user to the homepage after logout
    return redirect("/")

@app.route("/profile")
def profile():
    """User profile route."""

    # Retrieve the user ID from the session (assuming the user is logged in)
    user_id = session.get("user_id")

    if user_id:
        # Get the user from the database based on the user ID
        user = get_user_by_id(user_id)

        if user:
            return render_template("profile.html", user=user)
        else:
            # When the user doesn't exist or is not logged in, go back to the log-in page
            return redirect("/login")
    else:
        return redirect("/login")

@app.route("/profile-pic", methods=['POST'])
def profile_pic():
    """upload profile pic"""

    # Retrieve the user ID from the session (assuming the user is logged in)
    user_id = session.get("user_id")

    my_file = request.files['profile-pic']

    
    # Upload the original image to Cloudinary
    original_img_url = upload_to_cloudinary(my_file)
    
    # Perform skin color detection and get skin color values
    skin_color_values = detect_skin_color(original_img_url)

    print(user_id, "++++++++++++++")

    add_profile_pic(user_id,original_img_url)

    
    return jsonify({"original_url": original_img_url, "skin_color_values": skin_color_values})


@app.route('/async-media-upload-form')
def show_async_upload_form():
    """Show the async media upload form"""
    return render_template('async_upload_photo.html')

@app.route('/post-form-data-async', methods=['POST'])
def post_form_data_async():
    """Process form data and return the URLs generated by Cloudinary (original and skin detected)"""
    my_file = request.files['profile-pic']
    
    # Upload the original image to Cloudinary
    original_img_url = upload_to_cloudinary(my_file)
    
    # Perform skin color detection and get skin color values
    skin_color_values = detect_skin_color(original_img_url)
    
    return jsonify({"original_url": original_img_url, "skin_color_values": skin_color_values})

def upload_to_cloudinary(media_file):
    """Upload media file to Cloudinary"""
    result = cloudinary.uploader.upload(media_file, 
            api_key=CLOUDINARY_KEY, 
            api_secret=CLOUDINARY_SECRET, 
            cloud_name=CLOUD_NAME)
    return result['secure_url']

def detect_skin_color(image_url):
    """Perform skin color detection and return the skin color values"""
    image_cv = load_image_from_url(image_url)
    
    # Perform skin color detection using OpenCV
    skin_detected = perform_skin_detection(image_cv)
    
    # Get skin color values from the detected skin region
    skin_color_values = get_skin_color_values(skin_detected)
    
    return skin_color_values

def load_image_from_url(image_url):
    """Load image from URL using OpenCV"""
    response = requests.get(image_url).content
    image_data = np.frombuffer(response, dtype=np.uint8)
    image_cv = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
    return image_cv

def perform_skin_detection(image):
    # Implement your skin tone detection algorithm using OpenCV
    # Return the image with skin tones highlighted or detected
    
    # Example: Convert the image to HSV color space and apply a skin tone range
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    skin_mask = cv2.inRange(hsv_image, lower_skin, upper_skin)
    skin_detected = cv2.bitwise_and(image, image, mask=skin_mask)
    
    return skin_detected

def get_skin_color_values(skin_detected_image):
    # Convert the skin-detected image to grayscale
    gray_image = cv2.cvtColor(skin_detected_image, cv2.COLOR_BGR2GRAY)
    
    # Calculate mean and standard deviation of pixel values
    mean_val = np.mean(gray_image)
    std_val = np.std(gray_image)
    
    return {"mean": mean_val.item(), "std_dev": std_val.item()}



# Route to show the form for uploading a profile picture
"""@app.route("/upload-profile-pic", methods=["GET"])
def show_upload_form():
    return render_template("upload_photo.html")


# Route to process the uploaded profile picture
@app.route("/upload-profile-pic", methods=["POST"])
def upload_profile_pic():
    # Get the uploaded profile picture from the form data
    profile_pic = request.files['profile-pic']
    

    if profile_pic:
        # Make the Cloudinary API request to upload the profile picture
        #print('HELLLLOOOO')
        result = cloudinary.uploader.upload(
            profile_pic,
            api_key=CLOUDINARY_KEY, 
            api_secret=CLOUDINARY_SECRET, 
            cloud_name=CLOUD_NAME)
        print("GOODBYE")

        # Get the secure URL of the uploaded profile picture from the API response
        #profile_pic_url = result['secure_url']


        return f"Profile picture uploaded successfully! URL: {profile_pic_url}"
    else:
        return "No profile picture uploaded."

"""


#The quiz route
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    """Quiz route: Allows users to answer quiz questions and store their answers."""

    if request.method == "POST":
        # Retrieve the quiz answers from the form data
        quiz_question_1 = request.form.get("quiz_question_1")
        quiz_question_2 = request.form.get("quiz_question_2")
        quiz_question_3 = request.form.get("quiz_question_3")

        # Store the quiz answers in the session
        session["quiz_question_1"] = quiz_question_1
        session["quiz_question_2"] = quiz_question_2
        session["quiz_question_3"] = quiz_question_3

        # Redirect the user to the registration page after completing the quiz
        return redirect("/register")

    return render_template("quiz.html")

# Route for user to upload their tones and favorite products
@app.route("/library/upload", methods=['GET', 'POST'])
def upload_tones_and_products():
    if request.method == 'POST':
        skin_color = request.form['skin_color']
        hair_color = request.form['hair_color']
        eye_color = request.form['eye_color']
        product_name = request.form['product_name']
        price = request.form['price']
        shade = request.form['shade']
        category = request.form['category']
        description = request.form['description']
        brand = request.form['brand']
        sustainability = request.form['sustainability']
        free_of_animal_testing = request.form['free_of_animal_testing']
        eco_friendly = request.form['eco_friendly']
        vegan = request.form['vegan']

        color = create_color(skin_color, hair_color, eye_color)


        # Create product and associate color with it
        product = create_product(product_name, price, shade, category, description, brand, sustainability, free_of_animal_testing, eco_friendly, vegan, color)

        return redirect("/library")

    return render_template("upload_tones_products.html")



#The actual search route directed after the search filter route
@app.route("/search", methods=["GET", "POST"])
def search():
    """Search route: Allows users to filter products based on color."""

    if request.method == "POST":
        # Retrieve the color filters from the form data
        skin_color = request.form["skin_color"]
        eye_color = request.form["eye_color"]
        hair_color = request.form["hair_color"]

        # Perform the search using the search_products_by_color function
        products = search_products_by_color(skin_color, eye_color, hair_color)

        return render_template("search_results.html", products=products)

    return render_template("search.html")

@app.route("/recommend", methods=["GET"])
def recommend_products():
    user_skin_tone = request.args.get("skin_tone")

    # Filter products based on compatibility with user's skin tone
    recommended_products = []
    for product in mock_products:
        if "All" in product["skin_tones"] or user_skin_tone in product["skin_tones"]:
            recommended_products.append(product)

    return render_template("recommended_products.html", recommended_products=recommended_products)

"""@app.route('/messages/<int:user_id>')
def messages(user_id):
    user = User.query.get(user_id)
    if not user:
        return "User not found"
    
    messages = get_messages_for_user(user_id)
    return render_template('messages.html', user=user, messages=messages)

@socketio.on('send_message')
def handle_message(data):
    content = data['content']
    sender_id = data['sender_id']
    receiver_id = data['receiver_id']
    
    create_message(content, sender_id, receiver_id)
    
    emit('receive_message', data, broadcast=True)"""


if __name__ == "__main__":
    from model import connect_to_db, db

    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

