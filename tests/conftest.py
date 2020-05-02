"""Standard setup for fixtures to be used in Pytest.

We always instantiate the test Flask app for all our tests.

The `client` argument is available to every test run by pytest.
Simply pass in `client` as the last argument of a test method
and then call client.post() or client.get(), etc. It is used
in the same way as the requests library.

Subsequently, we also set up our database connection with regard for
Factory Boy, so that we rollback any changes made during the test
run. Ideas for connection() and test_session() were gleaned from
https://medium.com/@vittorio.camisa/agile-database-integration-tests-with-python-sqlalchemy-and-factory-boy-6824e8fe33a1
"""

"""Configuration/Fixtures for pytest unit tests."""
import os
import tempfile

import pytest
#from factory.base import FactoryMetaClass
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#import factories
import app


@pytest.fixture(autouse=True)
def client():
    """Provide access to the API via client.post, client.get, etc."""
    db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
    app.app.config['TESTING'] = True
    test_client = app.app.test_client()

    # Establish application context
    ctx = app.app.app_context()
    ctx.push()

#    with app.app.app_context():
#        app.init_db()

    yield test_client

    os.close(db_fd)
    os.unlink(app.app.config['DATABASE'])
    ctx.pop()


@pytest.fixture(scope='module')
def connection():
    """Set up a connection to the database."""
    engine = create_engine(os.environ['SQLALCHEMY_DATABASE_URI'])
    temp_connection = engine.connect()
    yield temp_connection
    temp_connection.close()


@pytest.fixture(scope='function')
def test_session(connection):
    """Set up a DB session for testing that rolls back after test."""
    # pylint:disable=protected-access,redefined-outer-name
    transaction = connection.begin()
    session_maker = sessionmaker()
    session = session_maker(bind=connection)

    # Assign this session to every factory for easier teardown
#    for attr in dir(factories):
#        class_attr = getattr(factories, attr)
#        if isinstance(class_attr, FactoryMetaClass):
#            class_attr._meta.sqlalchemy_session = session
#            class_attr._meta.sqlalchemy_session_persistence = None

    yield session
    session.close()
    transaction.rollback()
