import sqlalchemy as sa

from models import Base


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String(length=255))
    first_name = sa.Column(sa.String(length=255))
    last_name = sa.Column(sa.String(length=255))
    birthdate = sa.Column(sa.DateTime)

    def __repr__(self):
        return (f'<User {self.id} '
                f'({self.first_name} {self.last_name})>')
