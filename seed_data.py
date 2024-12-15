from app import create_app, db
from app.models import Author, Magazine, Article

# Initialize the app context
app = create_app()

def seed_data():
    with app.app_context():
        # Create sample authors
        author1 = Author(name="Author One")
        author2 = Author(name="Author Two")
        db.session.add(author1)
        db.session.add(author2)

        # Create sample magazines
        magazine1 = Magazine(name="Magazine One")
        magazine2 = Magazine(name="Magazine Two")
        db.session.add(magazine1)
        db.session.add(magazine2)

        # Create sample articles
        article1 = Article(title="Article One", author=author1, magazine=magazine1)
        article2 = Article(title="Article Two", author=author2, magazine=magazine2)
        db.session.add(article1)
        db.session.add(article2)

        # Commit changes to the database
        db.session.commit()
        print("Sample data added!")

if __name__ == "__main__":
    seed_data()
