"""Initialize the database with the tables defined in SQLAlchemy."""
import os
from datetime import datetime

import sqlalchemy as db

from app import db_session
from models import Base
from models.user import User


database_uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
try:
    engine = db.create_engine(database_uri, echo=True)
except TypeError:
    raise AttributeError('DB engine could not be initialized')

Base.metadata.create_all(engine)


user = User(
    email='afreestain@example.com',
    first_name='Amber',
    last_name='Freestain',
    birthdate=datetime(1980, 5, 6)
)

db_session.add(user)
db_session.commit()