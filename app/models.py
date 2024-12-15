from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    articles = db.relationship('Article', backref='author', lazy=True)

class Magazine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    articles = db.relationship('Article', backref='magazine', lazy=True)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    magazine_id = db.Column(db.Integer, db.ForeignKey('magazine.id'), nullable=False)
    
    author = db.relationship('Author', backref=db.backref('articles', lazy=True))
    magazine = db.relationship('Magazine', backref=db.backref('articles', lazy=True))
