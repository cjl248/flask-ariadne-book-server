import ipdb
from app import db
from .author_model import Author

def resolve_authors(obj, info):
    try:
        return [author for author in db.session.query(Author).all()]
    except Exception as error:
        return []

def resolve_author(obj, info, id):
    author = Author.query.get(id)
    if author:
        return author
    else:
        return None
