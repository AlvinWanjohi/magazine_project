from app.models import Author, Magazine

def get_articles_by_author(author_id):
    author = Author.query.get(author_id)
    if not author:
        return None, 'Author not found'
    articles = [{'id': article.id, 'title': article.title} for article in author.articles.all()]
    return articles, None

def get_articles_by_magazine(magazine_id):
    magazine = Magazine.query.get(magazine_id)
    if not magazine:
        return None, 'Magazine not found'
    articles = [{'id': article.id, 'title': article.title} for article in magazine.articles.all()]
    return articles, None
