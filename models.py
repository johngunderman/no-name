from database import Base, db_session

from sqlalchemy import Column, DateTime, Integer, SmallInteger, String, ForeignKey, Text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    password = Column(String(40))
    posts = relationship('Story', backref='user', lazy='dynamic')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User {0}>".format(self.username)

class Story(Base):
    __tablename__ = "story"
    id = Column(Integer, primary_key=True)
    poster_id = Column(Integer, ForeignKey('user.id'))
    href = Column(String(255))

    def __init__(self, poster_id, href):
        self.poster_id = poster_id
        self.href = href

    def __repr__(self):
        return "<Story #{0}>".format(self.href)
