from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from flask_migrate import Migrate

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config.from_object(Config)
db = SQLAlchemy(app)
db.create_all()
# migrate = Migrate(app, db)

from app import routes, models