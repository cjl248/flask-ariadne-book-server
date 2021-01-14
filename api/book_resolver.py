import ipdb
from app import db
from .book_model import Book
from .author_model import Author

def resolve_books(obj, info):
    try:
        return [book for book in db.session.query(Book).all()]
    except Exception as error:
        return []

def resolve_book(obj, info, id):
    book = Book.query.get(id)
    if book:
        return book
    else:
        return None

def add_book(obj, info, title, pages, author_id):
    author = Author.query.get(author_id)
    if not author:
        return {'success': False, 'book': None}
    book = Book(title=title, pages=pages, author_id=author_id)
    db.session.add(book)
    db.session.commit()
    if not book:
        return {'success': False, 'book': None}
    else:
        return {'success': True, 'book': book}
