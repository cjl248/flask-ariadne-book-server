import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/ariadne-books-api.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Welcome to my first GraphQL API!!!. Please navigate to \/graphql to query and mutate the SQLite database...'
