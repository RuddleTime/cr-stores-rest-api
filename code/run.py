from app import app
from db import db

db.init_app(app)

# SQLAlchemy will create the data.db file automatically, but
# needs to be told what tables and schemas to create in it
# Using a Flask decorator (not from an extension)

@app.before_first_request
def create_tables():
    # Creating tables in data.db (referenced above), if
    # they do not already exist
    db.create_all()
