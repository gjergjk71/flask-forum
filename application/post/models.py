from flask_sqlalchemy import SQLAlchemy
from application.thread.models import Thread
from application.authentication.models import User
from datetime import datetime

db = SQLAlchemy()

class Post(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	user_id = db.Column(db.Integer,db.ForeignKey(User.id))
	thread_id = db.Column(db.Integer,db.ForeignKey(Thread.id))
	content = db.Column(db.String)
	created_on = db.Column('created_on' , db.DateTime,default=datetime.utcnow())

	def __repr__(self):
		return f"<Post {self.id}"