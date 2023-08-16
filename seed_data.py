from server import app
from model import connect_to_db, db, User, Color, Product, Quiz, ProductColorAssociation

def seed_database():
    """Seed the database with mock data."""

    # Connect to the database
    connect_to_db(app)

    # Create all tables
    db.create_all()

    # Create mock users
    user1 = User(email="user1@example.com", password="password1", fname="Steve", lname="Doe")
    user2 = User(email="user2@example.com", password="password2", fname="Jane", lname="Smith")

    # Add users to the session
    db.session.add_all([user1, user2])

    # Commit the changes
    db.session.commit()

    # Create mock colors
    color1 = Color(skin_color="fair", hair_color="black", eye_color="brown", hexcode_id="#FFFFFF", user_id=user1.user_id)
    color2 = Color(skin_color="porcelain", hair_color="blonde", eye_color="blue", hexcode_id="#F0F0F0", user_id=user1.user_id)
    color3 = Color(skin_color="golden", hair_color="brown", eye_color="green", hexcode_id="#FFD700", user_id=user2.user_id)

    # Add colors to the session
    db.session.add_all([color1, color2, color3])

    # Commit the changes
    db.session.commit()

    # Create mock products
    product1 = Product(price=20, shade="Light", product_name="Loreal", category="Foundation", description="A light foundation for fair skin", brand="Brand A")
    product2 = Product(price=25, shade="Medium", product_name="Mac", category="Lipstick", description="A medium shade lipstick", brand="Brand B")
    product3 = Product(price=30, shade="Dark", product_name="Loreal", category="Eyeshadow", description="Dark eyeshadow palette", brand="Brand C")

    # Add products to the session
    db.session.add_all([product1, product2, product3])

    # Commit the changes
    db.session.commit()

    # Create associations between products and colors
    association1 = ProductColorAssociation(product_id=product1.product_id, tone_id=color1.tone_id)
    association2 = ProductColorAssociation(product_id=product2.product_id, tone_id=color2.tone_id)
    association3 = ProductColorAssociation(product_id=product3.product_id, tone_id=color3.tone_id)

    # Add associations to the session
    db.session.add_all([association1, association2, association3])

    # Commit the changes
    db.session.commit()

    print("Database seeded successfully!")

if __name__ == "__main__":
    with app.app_context():
        seed_database()
