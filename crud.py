from model import db, User, Color, Product, Rating,Quiz,ProductColorAssociation

def create_user(email, password, fname, lname, quiz_question_1=None, quiz_question_2=None, quiz_question_3=None):
    """Create and return a new user."""

    user = User(email=email, password=password, fname=fname, lname=lname)

    if quiz_question_1 and quiz_question_2 and quiz_question_3:
        quiz = Quiz(quiz_question_1=quiz_question_1, quiz_question_2=quiz_question_2, quiz_question_3=quiz_question_3)
        user.quiz = quiz

    db.session.add(user)

    db.session.commit()

    return user

def add_profile_pic(user_id, profile_pic_url):
    """Get user and set profile picture url for that user)"""

    user = User.query.get(user_id)
    user.profile_pic = profile_pic_url

    print("+++++++")

    db.session.add(user)

    db.session.commit()

    print(user_id, profile_pic_url)


def get_users():
    """Return all users."""
    return User.query.all()

def get_user_by_id(user_id):
    """Return a user by primary key."""
    return User.query.get(user_id)

def authenticate_user(email, password):
    """Authenticate the user based on email and password.
    Returns:
    - User object if authentication is successful
    - None if the user doesn't exist or password is incorrect
    """
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    return None

def create_color(skin_color, hair_color, eye_color):
    """Create and return a new color."""
    color = Color(skin_color=skin_color, hair_color=hair_color, eye_color=eye_color, hexcode_id=hexcode_id)
    return color

def get_colors():
    """Return all colors."""
    return Color.query.all()

def get_color_by_id(tone_id):
    """Return a color by primary key."""
    return Color.query.get(tone_id)

def create_product(price, shade, product_name, category, description, brand):
    """Create and return a new product."""

    product = Product(price=price, shade=shade, product_name=product_name, category=category,
                      description=description, brand=brand)
    return product

def get_products():
    """Return all products."""
    return Product.query.all()

def get_product_by_id(product_id):
    """Return a product by primary key."""
    return Product.query.get(product_id)

def search_products_by_color(skin_color, eye_color, hair_color):
    """Search products based on color filters."""

    # Query the products based on the color filters
    products = Product.query.join(Product.colors).filter(
        Color.skin_color == skin_color,
        Color.eye_color == eye_color,
        Color.hair_color == hair_color
    ).all()

    return products

def create_rating(user, product, score, rating_comment):
    """Create and return a new rating."""

    rating = Rating(user=user, product=product, score=score, rating_comment=rating_comment)
    return rating

def get_ratings():
    """Return all ratings."""
    return Rating.query.all()

def get_rating_by_id(rating_id):
    """Return a rating by primary key."""
    return Rating.query.get(rating_id)

def update_rating(rating_id, new_score, new_comment):
    """Update a rating's score and comment given the rating_id."""

    rating = Rating.query.get(rating_id)
    if rating:
        rating.score = new_score
        rating.rating_comment = new_comment

def delete_rating(rating_id):
    """Delete a rating given the rating_id."""

    rating = Rating.query.get(rating_id)
    if rating:
        db.session.delete(rating)

"""def create_message(content, sender_id, receiver_id):
    Create and return a new message.
    message = Message(content=content, sender_id=sender_id, receiver_id=receiver_id)
    db.session.add(message)
    db.session.commit()
    return message

def get_messages_for_user(user_id):
    Return messages sent to or received by the user.
    return Message.query.filter(
        (Message.sender_id == user_id) | (Message.receiver_id == user_id)
    ).all() """

if __name__ == "__main__":
    from server import app

    connect_to_db(app)
