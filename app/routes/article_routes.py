from flask import Blueprint, jsonify
from app.models import Article, Author, Magazine

article_routes = Blueprint('article_routes', __name__)

@article_routes.route('/articles')
def get_articles():
    articles = Article.query.all()
    return jsonify([{
        'id': article.id,
        'title': article.title,
        'author': article.author.name,
        'magazine': article.magazine.name
    } for article in articles])

@article_routes.route('/article/<int:article_id>')
def get_article(article_id):
    article = Article.query.get(article_id)
    if not article:
        return jsonify({'error': 'Article not found'}), 404
    return jsonify({
        'id': article.id,
        'title': article.title,
        'author': article.author.name,
        'magazine': article.magazine.name
    })
