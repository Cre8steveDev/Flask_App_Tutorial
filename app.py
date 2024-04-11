from flask import Flask
from blueprints.main_blueprint import main_views
from blueprints.auth_blueprint import auth_views

from flask_login import LoginManager
from models.database import db, user, User
from bson import ObjectId

# create an instance of the flask application
app = Flask(__name__)

app.secret_key = "ENTER_YOUR_SECRET_KEY"

app.register_blueprint(main_views)
app.register_blueprint(auth_views)

login = LoginManager(app)
login.login_view = "/login"

#setup the login user loader
@login.user_loader
def load_user(id):
	"""Confirm user exists in database then use else return None"""
	cur_user = user.find_one({"_id": ObjectId(id)})
	
	if cur_user is None:
		return None
	
	# Create a user instance from the retrieved user
	return User(cur_user.get("username"), str(cur_user.get("_id")))
