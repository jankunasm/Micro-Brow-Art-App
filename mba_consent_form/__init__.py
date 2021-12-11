from flask import Flask
from config import Config
from .site.routes import site
from .api.routes import api  # Very likely wont need this
from .authentication.routes import auth
from .consent.routes import cons
from .search.routes import searcher

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

from .models import db as root_db



app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(api) # Again Very likely wont need this
app.register_blueprint(auth)
app.register_blueprint(cons)
app.register_blueprint(searcher)

app.config.from_object(Config)

root_db.init_app(app)

migrate = Migrate(app, root_db)