from flask import Blueprint, jsonify
from app.models import Author

author_routes = Blueprint('author_routes', __name__)

@author_routes.route('/authors')
def get_authors():
    authors = Author.query.all()
    return jsonify([{'id': author.id, 'name': author.name} for author in authors])

@author_routes.route('/author/<int:author_id>/articles')
def get_author_articles(author_id):
    author = Author.query.get(author_id)
    if not author:
        return jsonify({'error': 'Author not found'}), 404

    articles = [{'id': article.id, 'title': article.title} for article in author.articles]
    return jsonify({'author': author.name, 'articles': articles})
