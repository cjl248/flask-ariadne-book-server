import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# run in command line: $ export FLASK_APP=main.py
app = Flask(__name__)
# Database connection
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/ariadne-books-api.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# CORS settings
cors = CORS(app, resources={r"/graphql/*": {"origins": "*"}})

db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Welcome to my first GraphQL API!!!. Please navigate to \/graphql to query and mutate the SQLite database...'
