from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import Column

from models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(sa.Integer, primary_key=True, autoincrement=True)
    email = Column(sa.String(length=255))
    first_name = Column(sa.String(length=255))
    last_name = Column(sa.String(length=255))
    password = Column(sa.String(length=255))
    created_ts = Column(sa.DateTime, default=datetime.now, nullable=False)

    def __repr__(self):
        return (f'<User {self.id} '
                f'({self.first_name} {self.last_name})>')
