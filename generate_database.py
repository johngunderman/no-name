#!/usr/bin/env python

import bcrypt
from server import db
from server import User

db.create_all()

t = User('tom', bcrypt.hashpw('password', bcrypt.gensalt())) 
j = User('john', bcrypt.hashpw('password', bcrypt.gensalt())) 

db.session.add(t)
db.session.add(j)
db.session.commit()
