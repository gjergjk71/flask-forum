
from flask import Blueprint, render_template,redirect,request
from flask_login import LoginManager, UserMixin, login_required,current_user,login_user,logout_user
from .models import User,db
from .forms import LoginForm,RegisterForm
import bcrypt

auth = Blueprint('auth', __name__,template_folder="templates/auth")
login_manager = LoginManager()

@login_manager.user_loader
def load_user(ID):
	return User.query.get(ID)

@auth.route("/register",methods=["GET","POST"])
def register():
	if current_user.is_authenticated:
		return redirect("/index")
	form = RegisterForm(request.form)
	if request.method == "GET":
		return render_template("register.html",form=form)
	elif request.method == "POST":
		if not form.validate():
			return render_template('register.html',form=form,invalid_form=True)
		password = form.password.data
		hashed_password = bcrypt.hashpw(password.encode("utf8"),bcrypt.gensalt())
		user = User(username=form.username.data,
					email=form.email.data,
					password=hashed_password)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		return redirect("/index")

@auth.route('/login',methods=["GET","POST"])
def login():
	if current_user.is_authenticated:
		return redirect("/index")
	form = LoginForm(request.form)
	if request.method == "GET":
		return render_template('login.html',form=form)
	elif request.method == "POST":
		if not form.validate():
			return render_template('login.html',form=form,invalid_form=True)
		password = form.password.data
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			access = bcrypt.checkpw(password.encode('utf8'),user.password)
			if access:
				login_user(user)
		else:
			return render_template('login.html',form=form,
									invalid_credentials=True)			
