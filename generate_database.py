#!/usr/bin/env python

import bcrypt
import os
from server import db,app
from server import User, Story

os.remove("db.sqlite")

db.create_all()

t = User('tom', bcrypt.hashpw('password', bcrypt.gensalt())) 
j = User('john', bcrypt.hashpw('password', bcrypt.gensalt())) 

db.session.add(t)
db.session.add(j)

db.session.commit()

s1 = Story(t.id, 'This is story 1', 'http://google.com')
s2 = Story(t.id, 'Story 2 is much cooler!', 'http://tomdooner.com')
s3 = Story(j.id, 'This, story 3, is superior.', 'http://causes.com')
s4 = Story(j.id, 'Story 4 is the best! I think.', 'http://johngunderman.com')

db.session.add(s1)
db.session.add(s2)
db.session.add(s3)
db.session.add(s4)

db.session.commit()
