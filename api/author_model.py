from app import db

class Author(db.Model):
    __tablename__ = 'author'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    def get_id(self):
        return self.id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, new_name):
        self.first_name = new_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, new_name):
        self.last_name = new_name
