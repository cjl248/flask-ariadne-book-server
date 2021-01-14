import ipdb
from app import db
from .book_model import Book

def resolve_books(obj, info):
    try:
        return [book for book in db.session.query(Book).all()]
    except Exception as error:
        return []

def resolve_book(obj, info, id):
