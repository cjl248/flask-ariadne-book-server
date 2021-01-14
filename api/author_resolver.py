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

def add_author(obj, info, first_name, last_name):
    author = Author(first_name=first_name, last_name=last_name)
    db.session.add(author)
    db.session.commit()
    if author:
        payload = { 'success': True, 'author': author }
    else:
        payload = { 'success': False, 'author': None }
    return payload

def delete_author(obj, info, id):
    author = Author.query.get(id)
    if author:
        db.session.delete(author)
        db.session.commit()
        return {'success': True, 'author': author}
    else:
        return {'success': False, 'author': None}

def update_first_name(obj, info, id, name):
    author = Author.query.get(id)
    if author:
        author.set_first_name(name)
        db.session.add(author)
        db.session.commit()
        return { 'success': True, 'author': author }
    else:
        return { 'success': False, 'author': None }
    return

def update_last_name(obj, info, id, name):
    # TODO: update author first name
    author = Author.query.get(id)
    if author:
        author.set_last_name(name)
        db.session.add(author)
        db.session.commit()
        return { 'success': True, 'author': author }
    else:
        return { 'success': False, 'author': None }
    return
