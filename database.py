from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import bcrypt
import os


engine = create_engine('sqlite:///db.sqlite', convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    ##TESTING MODE ONLY, DO NOT KEEP WHEN LIVE
    os.remove("db.sqlite")

    Base.metadata.create_all(bind=engine)
    insert_test_data()


def insert_test_data():
    from models import User, Story, Vote, Comment

    '''
    Add the users...
    '''

    t = User('tom', bcrypt.hashpw('password', bcrypt.gensalt()))
    j = User('john', bcrypt.hashpw('password', bcrypt.gensalt()))
    j2 = User('john2', bcrypt.hashpw('password', bcrypt.gensalt()))
    t2 = User('tom2', bcrypt.hashpw('password', bcrypt.gensalt()))

    db_session.add(t)
    db_session.add(t2)
    db_session.add(j)
    db_session.add(j2)

    db_session.commit()

    '''
    Add the stories...
    '''

    s1 = Story(t.id, 'This is story 1', 'http://google.com')
    s2 = Story(t.id, 'Story 2 is much cooler!', 'http://tomdooner.com')
    s3 = Story(j.id, 'This, story 3, is superior.', 'http://causes.com')
    s4 = Story(j.id, 'Story 4 is the best! I think.', 'http://johngunderman.com')

    db_session.add(s1)
    db_session.add(s2)
    db_session.add(s3)
    db_session.add(s4)

    db_session.commit()

    '''
    Add the votes...
    '''

    v1 = Vote(t.id, s1.id)
    v2 = Vote(t.id, s2.id)
    v3 = Vote(t.id, s3.id)
    v4 = Vote(t2.id, s2.id)
    v5 = Vote(t2.id, s3.id)
    v6 = Vote(j.id, s2.id)
    v7 = Vote(j.id, s3.id)
    v8 = Vote(j.id, s4.id)
    v9 = Vote(j2.id, s3.id)
    v10 = Vote(j2.id, s4.id)

    db_session.add(v1)
    db_session.add(v2)
    db_session.add(v3)
    db_session.add(v4)
    db_session.add(v5)
    db_session.add(v6)
    db_session.add(v7)
    db_session.add(v8)
    db_session.add(v9)
    db_session.add(v10)

    db_session.commit()

    ## comments

    c1 = Comment(j.id, s1.id, "This story stucks", None)
    c2 = Comment(j.id, s1.id, "This story stucks even more", None)
    c3 = Comment(j.id, s1.id, "Your site is broken", None)
    c4 = Comment(j.id, s1.id, "I like this cheesecake", None)

    db_session.add(c1)
    db_session.add(c2)
    db_session.add(c3)
    db_session.add(c4)

    db_session.commit()
