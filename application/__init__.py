from flask import Flask,request
from application.authentication.auth import auth,login_manager
from application.category.category import category
from application.forum.forum import forum
from application.thread.thread import thread
from application.post.post import post
from application.authentication.models import db as auth_db
from application.category.models import db as category_db
from application.forum.models import db as forum_db
from application.thread.models import db as thread_db
from application.post.models import db as post_db
from application.category.cbv import CreateCategory
from application.forum.cbv import CreateForum
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}/db.sqlite3'.format(str(os.getcwd()))
app.config.from_object(os.environ.get('SETTINGS'))
app.secret_key = os.urandom(24)

with app.app_context():
	login_manager.init_app(app)

	auth_db.init_app(app)
	category_db.init_app(app)
	forum_db.init_app(app)
	thread_db.init_app(app)
	post_db.init_app(app)

	auth_db.create_all()
	category_db.create_all()
	forum_db.create_all()
	thread_db.create_all()
	post_db.create_all()

	app.add_url_rule('/category/create', view_func=CreateCategory.as_view('CreateCategory'))
	app.add_url_rule('/forum/create/<string:category_slug>', view_func=CreateForum.as_view('CreateForum'))


app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(category,url_prefix="/category")
app.register_blueprint(forum,url_prefix="/forum")
app.register_blueprint(thread,url_prefix="/thread")
app.register_blueprint(post,url_prefix="/post")