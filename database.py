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
    from models import User, Story

    t = User('tom', bcrypt.hashpw('password', bcrypt.gensalt()))
    j = User('john', bcrypt.hashpw('password', bcrypt.gensalt()))

    db_session.add(t)
    db_session.add(j)

    db_session.commit()

    s1 = Story(t.id, 'This is story 1', 'http://google.com')
    s2 = Story(t.id, 'Story 2 is much cooler!', 'http://tomdooner.com')
    s3 = Story(j.id, 'This, story 3, is superior.', 'http://causes.com')
    s4 = Story(j.id, 'Story 4 is the best! I think.', 'http://johngunderman.com')

    db_session.add(s1)
    db_session.add(s2)
    db_session.add(s3)
    db_session.add(s4)

    db_session.commit()
