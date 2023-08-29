from server import app
from model import connect_to_db, db, User, Color, Product, Quiz, ProductColorAssociation
import os

def seed_database():
    """Seed the database with mock data."""

    os.system('dropdb makeups')
    os.system('createdb makeups')

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
    color1 = Color(skin_color="#FCE5D8", hair_color="#FFF5E1", eye_color="#006400", user_id=user1.user_id)
    color2 = Color(skin_color="#240B03", hair_color="#E5B887", eye_color="#0D98BA", user_id=user1.user_id)
    color3 = Color(skin_color="#512913", hair_color="#C04000", eye_color="#B2BEB5", user_id=user2.user_id)
    color4 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color5 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color6 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color7 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color8 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color9 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color10 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color11 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color12 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color13 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color14 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color15 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color16 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color17 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color18 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color19 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color20 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color21 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color22 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color23 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color24 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color25 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color26 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)
    color27 = Color(skin_color="#240B03", hair_color="#7B4B26", eye_color="#000000", user_id=user1.user_id)


    # Add colors to the session
    db.session.add_all([color1, color2, color3, color4, color5, color6, color7,
    color8, color9, color10, color11, color12, color13, color14,
    color15, color16, color17, color18, color19, color20, color21,
    color22, color23, color24, color25, color26, color27])

    # Commit the changes
    db.session.commit()

    # Create mock products
    product1 = Product(price=20, shade="Light", product_name="Loreal", category="Foundation", description="A light foundation for fair skin", brand="Brand A")
    product2 = Product(price=25, shade="Medium", product_name="Mac", category="Lipstick", description="A medium shade lipstick", brand="Brand B")
    product3 = Product(price=30, shade="Dark", product_name="Loreal", category="Eyeshadow", description="Dark eyeshadow palette", brand="Brand C")
    product4 = Product(price=34, shade="Warm Tan", product_name="Benefit Hoola Bronzer", category="Bronzer", description="Matte bronzer for a natural sun-kissed look", brand="Benefit")
    product5 = Product(price=29, shade="Golden", product_name="Physicians Formula Butter Bronzer", category="Bronzer", description="Infused with Murumuru butter for a buttery texture", brand="Physicians Formula")
    product6 = Product(price=32, shade="Deep Bronze", product_name="Fenty Beauty Sun Stalk'r Instant Warmth Bronzer", category="Bronzer", description="Long-wearing bronzer for all skin tones", brand="Fenty Beauty")
    product7 = Product(price=22, shade="Peachy Pink", product_name="Milani Baked Blush", category="Blush", description="Baked blush with a hint of shimmer", brand="Milani")
    product8 = Product(price=18, shade="Rose", product_name="Tarte Amazonian Clay Blush", category="Blush", description="Long-wearing blush with a silky texture", brand="Tarte")
    product9 = Product(price=26, shade="Coral", product_name="NARS Blush", category="Blush", description="Iconic powder blush for a natural flush", brand="NARS")
    product10 = Product(price=12, shade="Spice", product_name="MAC Lip Pencil", category="Lip Liner", description="Creamy lip pencil for precise lining", brand="MAC")
    product11 = Product(price=9, shade="Mauve", product_name="NYX Professional Slim Lip Pencil", category="Lip Liner", description="Slim pencil for defining and shaping lips", brand="NYX Professional Makeup")
    product12 = Product(price=14, shade="Nude", product_name="Charlotte Tilbury Lip Cheat Lip Liner", category="Lip Liner", description="Velvety lip liner for fuller-looking lips", brand="Charlotte Tilbury")
    product13 = Product(price=28, shade="Chestnut", product_name="Fenty Beauty Mattemoiselle Plush Matte Lipstick", category="Lipstick", description="Intense color with a soft matte finish", brand="Fenty Beauty")
    product14 = Product(price=25, shade="Brick Red", product_name="Urban Decay Vice Lipstick", category="Lipstick", description="Creamy lipstick with a wide range of shades", brand="Urban Decay")
    product15 = Product(price=22, shade="Mauve", product_name="Anastasia Beverly Hills Matte Lipstick", category="Lipstick", description="Full-pigment lipstick with a comfortable matte finish", brand="Anastasia Beverly Hills")
    product16 = Product(price=20, shade="Brunette", product_name="Anastasia Beverly Hills Brow Wiz", category="Eyebrow", description="Ultra-fine brow pencil for precise application", brand="Anastasia Beverly Hills")
    product17 = Product(price=16, shade="Dark Brown", product_name="NYX Professional Micro Brow Pencil", category="Eyebrow", description="Micro-tip pencil for filling and shaping brows", brand="NYX Professional Makeup")
    product18 = Product(price=18, shade="Taupe", product_name="Benefit Precisely, My Brow Pencil", category="Eyebrow", description="Ultra-fine brow defining pencil", brand="Benefit")
    product19 = Product(price=24, shade="Black", product_name="Too Faced Better Than Sex Mascara", category="Mascara", description="Volumizing mascara for dramatic lashes", brand="Too Faced")
    product20 = Product(price=21, shade="Carbon Black", product_name="L'Oréal Voluminous Carbon Black Mascara", category="Mascara", description="Intense black mascara for bold lashes", brand="L'Oréal")
    product21 = Product(price=26, shade="Brown", product_name="Benefit They're Real! Lengthening Mascara", category="Mascara", description="Lengthening mascara for defined lashes", brand="Benefit")
    product22 = Product(price=18, shade="Brown", product_name="Stila Stay All Day Waterproof Liquid Eyeliner", category="Eyeliner", description="Precision liquid eyeliner for long-lasting wear", brand="Stila")
    product23 = Product(price=14, shade="Blackest Black", product_name="Maybelline Eye Studio Master Precise Liquid Eyeliner", category="Eyeliner", description="Felt-tip liner for sharp lines", brand="Maybelline")
    product24 = Product(price=16, shade="Navy", product_name="Urban Decay Perversion Waterproof Fine-Point Eye Pen", category="Eyeliner", description="Waterproof eye pen for bold lines", brand="Urban Decay")
    product25 = Product(price=40, shade="Golden Beige", product_name="Estée Lauder Double Wear Stay-in-Place Foundation", category="Foundation", description="Long-wearing foundation with buildable coverage", brand="Estée Lauder")
    product26 = Product(price=28, shade="Natural Ivory", product_name="L'Oréal Infallible Pro-Glow Foundation", category="Foundation", description="Radiant finish foundation with all-day wear", brand="L'Oréal")
    product27 = Product(price=36, shade="Warm Sand", product_name="NARS Sheer Glow Foundation", category="Foundation", description="Sheer foundation with a natural-looking finish", brand="NARS")
    
    # Add products to the session
    db.session.add_all([product1, product2, product3, product4, product5, product6, product7,
    product8, product9, product10, product11, product12, product13, product14,
    product15, product16, product17, product18, product19, product20, product21,
    product22, product23, product24, product25, product26, product27])

    # Commit the changes
    db.session.commit()

    # Create associations between products and colors
    association1 = ProductColorAssociation(product_id=product1.product_id, tone_id=color1.tone_id)
    association2 = ProductColorAssociation(product_id=product2.product_id, tone_id=color2.tone_id)
    association3 = ProductColorAssociation(product_id=product3.product_id, tone_id=color3.tone_id)
    association4 = ProductColorAssociation(product_id=product4.product_id, tone_id=color4.tone_id)
    association5 = ProductColorAssociation(product_id=product5.product_id, tone_id=color5.tone_id)
    association6 = ProductColorAssociation(product_id=product6.product_id, tone_id=color6.tone_id)
    association7 = ProductColorAssociation(product_id=product7.product_id, tone_id=color7.tone_id)
    association8 = ProductColorAssociation(product_id=product8.product_id, tone_id=color8.tone_id)
    association9 = ProductColorAssociation(product_id=product9.product_id, tone_id=color9.tone_id)
    association10 = ProductColorAssociation(product_id=product10.product_id, tone_id=color10.tone_id)
    association11 = ProductColorAssociation(product_id=product11.product_id, tone_id=color11.tone_id)
    association12 = ProductColorAssociation(product_id=product12.product_id, tone_id=color12.tone_id)
    association13 = ProductColorAssociation(product_id=product13.product_id, tone_id=color13.tone_id)
    association14 = ProductColorAssociation(product_id=product14.product_id, tone_id=color14.tone_id)
    association15 = ProductColorAssociation(product_id=product15.product_id, tone_id=color15.tone_id)
    association16 = ProductColorAssociation(product_id=product16.product_id, tone_id=color16.tone_id)
    association17 = ProductColorAssociation(product_id=product17.product_id, tone_id=color17.tone_id)
    association18 = ProductColorAssociation(product_id=product18.product_id, tone_id=color18.tone_id)
    association19 = ProductColorAssociation(product_id=product19.product_id, tone_id=color19.tone_id)
    association20 = ProductColorAssociation(product_id=product20.product_id, tone_id=color20.tone_id)
    association21 = ProductColorAssociation(product_id=product21.product_id, tone_id=color21.tone_id)
    association22 = ProductColorAssociation(product_id=product22.product_id, tone_id=color22.tone_id)
    association23 = ProductColorAssociation(product_id=product23.product_id, tone_id=color23.tone_id)
    association24 = ProductColorAssociation(product_id=product24.product_id, tone_id=color24.tone_id)
    association25 = ProductColorAssociation(product_id=product25.product_id, tone_id=color25.tone_id)
    association26 = ProductColorAssociation(product_id=product26.product_id, tone_id=color26.tone_id)
    association27 = ProductColorAssociation(product_id=product27.product_id, tone_id=color27.tone_id)


    # Add associations to the session
    db.session.add_all([association1, association2, association3, association4, association5,
    association6, association7, association8, association9, association10,
    association11, association12, association13, association14, association15,
    association16, association17, association18, association19, association20,
    association21, association22, association23, association24, association25,
    association26, association27])

    # Commit the changes
    db.session.commit()

    print("Database seeded successfully!")

if __name__ == "__main__":
    with app.app_context():
        seed_database()
