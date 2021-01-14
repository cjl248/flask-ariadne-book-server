import ipdb
from app import db
from .author_model import Author

def resolve_authors(obj, info):
    try:
        # ipdb.set_trace()
        authors = [author for author in db.session.query(Author).all()]
        # payload = { 'success': True, 'authors': authors }
        return authors
    except Exception as error:
        # payload = { 'success': False, 'errors': str(error) }
        return []
    # return payload
