from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///magazine.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)

    # Register blueprints
    from app.routes.author_routes import author_routes
    from app.routes.magazine_routes import magazine_routes
    from app.routes.article_routes import article_routes

    app.register_blueprint(author_routes)
    app.register_blueprint(magazine_routes)
    app.register_blueprint(article_routes)

    return app
