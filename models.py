from database import Base, db_session

from sqlalchemy import Column, DateTime, Integer, SmallInteger, String, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    password = Column(String(40))
    posts = relationship('Story', backref='user', lazy='dynamic')
    votes = relationship('Vote', backref='user', lazy='dynamic')
    comments = relationship('Comment', backref='user', lazy='dynamic')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User {0}>".format(self.username)

class Story(Base):
    __tablename__ = "story"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    poster_id = Column(Integer, ForeignKey('user.id'))
    href = Column(String(255))
    votes = relationship('Vote', backref='story', lazy='dynamic')
    comments = relationship('Comment', backref='story', lazy='dynamic')

    def __init__(self, poster_id, title, href):
        self.poster_id = poster_id
        self.title = title
        self.href = href

    def __repr__(self):
        return "<Story #{0}>".format(self.href)

class Vote(Base):
    __tablename__ = "vote"
    __table_args__ = (
        UniqueConstraint('user_id', 'story_id'),
    )
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    story_id = Column(Integer, ForeignKey('story.id'))
    direction = Column(Integer)

    def __init__(self, user_id, story_id, direction):
        self.user_id = user_id
        self.story_id = story_id
        self.direction = direction

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    story_id = Column(Integer, ForeignKey('story.id'))
    content = Column(Text)

    def __init__(self, user_id, story_id, content, parent):
        self.user_id = user_id
        self.story_id = story_id
        self.content = content
        self.parent = parent

