from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    profile_pic = db.Column(db.String, nullable=True)

    # One to one relationship with Quiz(one quiz per one user)
    # Uselist=False species the one to one relationship
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.quiz_id'))
    quiz = db.relationship('Quiz', back_populates='user', uselist=False)

    # One-to-many relationship with Color (One user can have multiple colors)
    colors = db.relationship('Color', back_populates='user')

    # One-to-many relationship with Rating (One user can have multiple ratings)
    ratings = db.relationship('Rating', back_populates='user')

    """# One-to-many relationship with Message (One user can send/receive multiple messages)
    messages_sent = db.relationship('Message', back_populates='sender', foreign_keys='Message.sender_id')
    messages_received = db.relationship('Message', back_populates='receiver', foreign_keys='Message.receiver_id')"""

    def __init__(self, email, password, fname, lname):
        self.email = email
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        self.fname = fname
        self.lname = lname
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User(user_id={self.user_id}, fname={self.fname}, lname={self.lname})>"


class Color(db.Model):
    __tablename__ = "color"

    tone_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    skin_color = db.Column(db.String, nullable=False)
    hair_color = db.Column(db.String, nullable=False)
    eye_color = db.Column(db.String, nullable=False)
    hexcode_id = db.Column(db.String)

    # Foreign key column
    # Establishing the one to many relationship with the User class
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    user = db.relationship('User', back_populates='colors')

    # Many-to-many relationship with Product through ProductColorAssociation
    products = db.relationship('Product', secondary='product_color_association', back_populates='colors')

    def __repr__(self):
        return f"<Color(tone_id={self.tone_id}, hexcode_id={self.hexcode_id})>"

class Product(db.Model):
    __tablename__ = "products"

    product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    shade = db.Column(db.String, nullable=False)
    product_name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    brand = db.Column(db.String, nullable=False)
    sustainability = db.Column(db.String, nullable=True)
    free_of_animal_testing = db.Column(db.String, nullable=True)
    eco_friendly = db.Column(db.String, nullable=True)
    vegan = db.Column(db.String, nullable=True)

    # Many-to-many relationship with Color through ProductColorAssociation
    colors = db.relationship('Color', secondary='product_color_association', back_populates='products')

    # One-to-many relationship with Rating (One product can have multiple ratings)
    ratings = db.relationship('Rating', back_populates='product')

    def __repr__(self):
        return f"<Product(product_id={self.product_id}, product_name={self.product_name})>"

class ProductColorAssociation(db.Model):
    __tablename__ = 'product_color_association'

    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), primary_key=True)
    tone_id = db.Column(db.Integer, db.ForeignKey('color.tone_id'), primary_key=True)

    def __repr__(self):
        return f"<ProductColorAssociation(product_id={self.product_id}, tone_id={self.tone_id})>"

class Quiz(db.Model):
    __tablename__ = "quiz"

    quiz_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    quiz_question_1 = db.Column(db.String)
    quiz_question_2 = db.Column(db.String)
    quiz_question_3 = db.Column(db.String)

    # One to one relationship with User
    user = db.relationship('User', back_populates='quiz', uselist=False)

    def __repr__(self):
        return f"<Quiz(quiz_id={self.quiz_id})>"

class Rating(db.Model):
    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    score = db.Column(db.Integer, nullable=False)
    rating_comment = db.Column(db.Text)

    # Establishing the relationship with the User class
    user = db.relationship('User', back_populates='ratings')

    # Establishing the relationship with the Product class
    product = db.relationship('Product', back_populates='ratings')

    def __repr__(self):
        return f"<Rating(rating_id={self.rating_id}, score={self.score})>"

"""class Message(db.Model):
    __tablename__ = "messages"

    message_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    def __repr__(self):
        return f"<Message(message_id={self.message_id}, sender_id={self.sender_id}, receiver_id={self.receiver_id}, timestamp={self.timestamp})>" """



def connect_to_db(flask_app, db_uri="postgresql://localhost:5432/makeups", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
