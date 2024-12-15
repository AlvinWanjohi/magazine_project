from flask import Blueprint, jsonify
from app.models import Author, Magazine

article_routes = Blueprint('article_routes', __name__)

# Route to get all articles by a specific author
@article_routes.route('/author/<int:author_id>/articles')
def get_author_articles(author_id):
    author = Author.query.get(author_id)
    if not author:
        return jsonify({'error': 'Author not found'}), 404

    articles = [{'id': article.id, 'title': article.title} for article in author.articles]
    return jsonify({'author': author.name, 'articles': articles})

# Route to get all articles from a specific magazine
@article_routes.route('/magazine/<int:magazine_id>/articles')
def get_magazine_articles(magazine_id):
    magazine = Magazine.query.get(magazine_id)
    if not magazine:
        return jsonify({'error': 'Magazine not found'}), 404

    articles = [{'id': article.id, 'title': article.title} for article in magazine.articles]
    return jsonify({'magazine': magazine.name, 'articles': articles})
