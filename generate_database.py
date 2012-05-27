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

s1 = Story(t.id, 'This is story 1')
s2 = Story(t.id, 'Story 2 is much cooler!')
s3 = Story(j.id, 'This, story 3, is superior.')
s4 = Story(j.id, 'Story 4 is the best! I think.')

db.session.add(s1)
db.session.add(s2)
db.session.add(s3)
db.session.add(s4)

db.session.commit()
