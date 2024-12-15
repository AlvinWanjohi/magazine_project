from flask import Blueprint, jsonify
from app.models import Magazine

magazine_routes = Blueprint('magazine_routes', __name__)

@magazine_routes.route('/magazines')
def get_magazines():
    magazines = Magazine.query.all()
    return jsonify([{'id': magazine.id, 'name': magazine.name} for magazine in magazines])

@magazine_routes.route('/magazine/<int:magazine_id>/articles')
def get_magazine_articles(magazine_id):
    magazine = Magazine.query.get(magazine_id)
    if not magazine:
        return jsonify({'error': 'Magazine not found'}), 404

    articles = [{'id': article.id, 'title': article.title} for article in magazine.articles]
    return jsonify({'magazine': magazine.name, 'articles': articles})
