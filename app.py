from flask import Flask
from blueprints.main_blueprint import main_views
from blueprints.auth_blueprint import auth_views

# create an instance of the flask application
app = Flask(__name__)

app.register_blueprint(main_views)
app.register_blueprint(auth_views)
