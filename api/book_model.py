from app import db
from sqlalchemy.orm import relationship

class Book(db.Model):

    __tablename__ = 'book'

    author_id = db.Column(
        db.Integer,
        db.ForeignKey('author.id', ondelete='CASCADE'),
        nullable=False
    )
    author = db.relationship('Author', backref='books')
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    pages = db.Column(db.Integer)
