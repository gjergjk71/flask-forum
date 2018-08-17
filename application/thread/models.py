from flask_sqlalchemy import SQLAlchemy
from application.forum.models import Forum
from application.authentication.models import User
db = SQLAlchemy()

class Thread(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	forum_id = db.Column(db.Integer,db.ForeignKey(Forum.id))
	user_id = db.Column(db.Integer,db.ForeignKey(User.id))
	title = db.Column(db.String(150))
	description = db.Column(db.String)
	def __repr__(self):
		return f"<Thread {self.id}>"
