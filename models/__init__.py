"""Provides access to the database via SQLAlchemy and defines the data models."""
import os

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


def init_db(app):
    """Initialize the database session for accessing it.

    Attempt to get the URI from the Docker container, falling
    back to the OS environment variable if that fails.
    """
    global engine
    global session

    database_uri = app.config.get(
        'SQLALCHEMY_DATABASE_URI',
        os.environ.get('SQLALCHEMY_DATABASE_URI')
    )

    try:
        engine = sa.create_engine(database_uri)
    except TypeError:
        raise AttributeError('DB engine could not be initialized')

    session.configure(bind=engine)

    # Allow for Model.query. as an alternative to session.query(Model).
    Base.query = session.query_property()

    return session


Base = declarative_base()
session_factory = sa.orm.sessionmaker()
engine = None
session = sa.orm.scoped_session(session_factory)
